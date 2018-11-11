from urllib.request import Request, urlopen
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from flask import request, jsonify, Blueprint, current_app as app
import json

import re

class MediumResource(Resource):
    def post(self):
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400
        url = request.json.get('url', None)
        req = Request(url,
            data=None, 
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            })
        content = str(urlopen(req).read())
        post = re.search('(?<="post":)(.*)(?=,"postLayout)', content).group(0)
        post = post.replace('\\', '\\\\')
        post_json = json.loads(post)
        m4a_url = post_json["audioVersionUrl"]
        if m4a_url:
            return {"mp4": m4a_url}
        return {"message": "File not found"}
        
        