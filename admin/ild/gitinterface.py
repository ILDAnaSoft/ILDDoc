"""
interface to github via CURL

"""

import json
from logging import getLogger
from collections import OrderedDict, defaultdict
import re

from pprint import pprint
from operator import itemgetter

from helperfunctions import parseForReleaseNotes, curl2Json, \
                            authorMapping, versionComp

from parseversion import Version

__RCSID__ = None

class Repo(object):
  """ class representing a given repository"""

  def __init__( self, owner, repo, branch='master', dryRun=True):
    self.owner = owner
    self.repo = repo
    self.branch = branch
    self._options = dict( owner=self.owner, repo=self.repo  )
    self.log = getLogger( repo )

  def __str__( self ):
    return self.owner+"/"+self.repo

  def _githubAPI( self , ressource ):
    return "https://api.github.com/" + ressource

  def _github( self, action ):
    """ return the url to perform actions on github

    :param str action: command to use in the gitlab API, see documentation there
    :returns: url to be used by curl
    """
    options = dict(self._options)
    options["action"] = action
    ghURL = self._githubAPI("repos/%(owner)s/%(repo)s/%(action)s" % options)
    return ghURL


  def getGithubPRs( self, state="open", mergedOnly=False, perPage=100):
    """ get all PullRequests from github

    :param str state: state of the PRs, open/closed/all, default open
    :param bool merged: if PR has to be merged, only sensible for state=closed
    :returns: list of githubPRs
    """
    url = self._github( "pulls?state=%s&per_page=%s" % (state, perPage) )
    prs = curl2Json(url=url)
    #pprint(prs)
    if not mergedOnly:
      return prs

    ## only merged PRs
    prsToReturn = []
    for pr in prs:
      if pr.get( 'merged_at', None ) is not None:
        prsToReturn.append(pr)

    return prsToReturn

  def getGithubTags( self):
    """ get all tags from github

    u'commit': {u'sha': u'49680c32f9c0734dcbf0efe2f01e2363dab3c64e',
                u'url': u'https://api.github.com/repos/andresailer/Marlin/commits/49680c32f9c0734dcbf0efe2f01e2363dab3c64e'},
    u'name': u'v01-02-01',
    u'tarball_url': u'https://api.github.com/repos/andresailer/Marlin/tarball/v01-02-01',
    u'zipball_url': u'https://api.github.com/repos/andresailer/Marlin/zipball/v01-02-01'},

    :returns: list of tags
    """
    result = curl2Json(url=self._github("tags"))
    if isinstance( result, dict ) and 'Not Found' in result.get('message'):
      raise RuntimeError( "Package not found: %s" % str(self) )
    return result

  def getGithubReleases( self):
    """ get the last few releases from github

    :returns: list of releases
    """
    result = curl2Json(url=self._github("releases"))
    #pprint(result)
    return result


  def getHeadOfBranch( self ):
    """return the commit sha of the head of the branch"""
    result = curl2Json(url=self._github("git/refs/heads/%s" % self.branch))
    if 'message' in result:
      raise RuntimeError( "Error:",result['message'] )

    commitsha = result['object']['sha']

    return commitsha
    ## also get the sha of the tree

  def getTreeShaForCommit( self, commit ):
    """ return the sha of the tree for given commit"""
    result = curl2Json(self._github( "git/commits/%s" % commit))
    if 'sha' not in result:
      raise RuntimeError( "Error: Commit not found" )
    treesha = result['tree']['sha']
    return treesha


  def getFileFromBranch( self, filename ):
    """return the content of the file in the given branch, filename needs to be the full path"""
    result = curl2Json(url=self._github( "contents/%s?ref=%s" %(filename, self.branch)))
    encoded = result.get( 'content', None )
    if encoded is None:
      self.log.error( "File %s not found for %s", filename, self )
      raise RuntimeError( "File not found" )
    content = encoded.decode("base64")
    sha = result['sha']
    return content, sha, encoded


  def createGithubCommit( self, filename, fileSha, content, message ):
    """
    create a commit on the repository with `version` and on `branch`, makes tag on last commit of the branch

    :param str treeSha: sha of the tree the commit will go
    :param str filename: full path to the file
    :param str content: base64 encoded content of the file


    PUT /repos/:owner/:repo/contents/:path

    Parameters
    Name  Type  Description
    path  string  Required. The content path.
    message   string  Required. The commit message.
    content   string  Required. The updated file content, Base64 encoded.
    sha   string  Required. The blob SHA of the file being replaced.
    branch  string  The branch name. Default: the repository's default branch (usually master)
    Optional Parameters

    """
    coDict = dict( path=filename, content=content, branch=self.branch, sha=fileSha, message=message, force='true' )

    result = curl2Json(requestType='PUT', parameterDict=coDict,
                       url=self._github("contents/%s" % filename))

    if 'commit' not in result:
      raise RuntimeError( "Failed to update file: %s" % result['message'] )

    return result

    
  def addCollaborator( self, user ):
    """ add a collaborator to this repository """
    addDict = dict(permission="push")
    result = curl2Json(requestType="PUT", parameterDict=addDict, url=self._githubAPI("repos/{0}/{1}/collaborators/{2}".format(self.owner, self.repo, user)))
    
    print result

  def formatSkeletonFiles( self , description ):
    """ format all template files of this repository. 
    Only work if it has been forked from the Skeleton repository """
    files = ["Readme.md", "CMakeLists.txt", "source/CMakeLists.txt"]
    fmtDict = dict(repository=self.repo, description=description)
    
    for f in files:
      self.formatFileAndCommit(fmtDict, f)
      
    # Set the repository description
    editDict = dict( name=self.repo, description=description )
    result = curl2Json(requestType="PATCH", parameterDict=editDict, url=self._githubAPI("repos/{0}/{1}".format(self.owner, self.repo)))
 
  def formatFileAndCommit( self, options, filen ):
    """ format the file `filen` with the `options` dictionary and create a new commit """
    content, sha, encodedOld = self.getFileFromBranch( filen )
    contentNew = content % options
    contentEncoded = contentNew.encode('base64')
    
    message = "Formated %s on creation" % filen
    self.createGithubCommit( filen, sha, contentEncoded, message=message )
    
