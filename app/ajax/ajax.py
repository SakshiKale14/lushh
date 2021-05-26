
import traceback
from flask import Flask , Blueprint, jsonify, request, abort
import time

ajax_bp = Blueprint("ajax_bp", __name__)

@ajax_bp.route("/search")
def search_query():
    
  
  
    return 'hi'
