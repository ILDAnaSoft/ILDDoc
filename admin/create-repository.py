#!/usr/bin/env python
"""

ILDAnaSoft repository creation script. Clone the skeleton repository and create a new repository from it.
This is an admin script and can be used only administrators of ILDAnaSoft github collaboration.

"""

from logging import getLogger
import logging
from pprint import pprint

import argparse

__RCSID__ = None

from ild.gitinterface import Repo
# from ild.helperfunctions import checkRate
from ild.helperfunctions import *

def _parsePrintLevel( level ):
  """ translate printlevel to logging level"""
  return dict( CRITICAL=logging.CRITICAL,
               ERROR=logging.ERROR,
               WARNING=logging.WARNING,
               INFO=logging.INFO,
               DEBUG=logging.DEBUG,
             )[level]

class ILDAnaSoftAdmin(object):
  """ Object to hold the interface to clone repo, create new repo, read command line options, etc"""

  def __init__( self ):
    self.owner = "ILDAnaSoft"
    self.repository = None
    self.printLevel = "INFO"
    self.user = None
    self.benchmark = False
    self.description = None
    self.log = getLogger( "ILDAnaSoft" )
    self.errors = []
    self.repo = None
    self.noCreate = False
    self.skeleton = None

  def abort( self ):
    """ print error messages and raise exception """
    for line in self.errors:
      self.log.error( "ERROR: %s", line )
    raise RuntimeError( "ERROR" )

  def parseOptions(self):
    """parse the command line options"""
    parser = argparse.ArgumentParser("Admin tool for ILDAnaSoft github collaboration",
                                     formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("-v", "--print-level", action="store", default=self.printLevel, dest="printLevel",
                        choices=('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'),
                        help="Verbosity DEBUG, INFO, WARNING, ERROR, CRITICAL")

    parser.add_argument("--repository", action="store", default=self.repository,
                        help="The new repository name")
                        
    parser.add_argument("--benchmark", action="store_true", dest="benchmark", default=self.benchmark,
                        help="Whether the repository is an ILD physics benchmark (add ILDbench_ to repository name)")
                        
    parser.add_argument("--no-create", action="store_true", dest="noCreate", default=self.noCreate,
                        help="Whether the skip repository creation")
                        
    parser.add_argument("--description", action="store", default=self.description,
                        help="The repository description")
    
    parser.add_argument("--user", action="store", default=self.user,
                        help="The github user name of the developer")


    parsed = parser.parse_args()

    self.printLevel = _parsePrintLevel( parsed.printLevel )
    logging.basicConfig( level=self.printLevel, format='%(levelname)-5s - %(name)-8s: %(message)s' )

    self.user = parsed.user
    self.description = parsed.description
    self.benchmark = parsed.benchmark
    self.repository = parsed.repository if not self.benchmark else "ILDbench_" + parsed.repository
    
    self._checkConsistency()

    if self.errors:
      self.abort()
    
    checkRate()

  def _checkConsistency( self ):
    if not self.repository:
      self.errors.append( "No repository name provided !" )    
      
    if not self.description:
      self.errors.append( "No repository description provided !" )
      
    
  def run( self ):
    """ execute everything """
    
    # Create the new repository
    if not self.noCreate:
      createRepository( self.owner, self.repository, self.description )
        
    # Copy the skeleton repository
    cloneAndPush( self.owner, "Skeleton", self.owner, self.repository )
    
    repo = Repo( self.owner, self.repository )
    
    if self.user:
      repo.addCollaborator( self.user )

    repo.formatSkeletonFiles( self.description )

if __name__ == "__main__":
  RUNNER = ILDAnaSoftAdmin()
  try:
    RUNNER.parseOptions()
  except RuntimeError as e:
    print ("Error during runtime: %s", e)
    exit(1)

  try:
    RUNNER.run()
  except RuntimeError as e:
    logging.error("Error during runtime: %s", e)
    exit(1)

