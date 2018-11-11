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
        audioVersionUrl = post_json["audioVersionUrl"]
        id = post_json["id"]
        title = post_json["title"]
        uniqueSlug = post_json["uniqueSlug"]
        webCanonicalUrl = post_json["webCanonicalUrl"]
        if audioVersionUrl:
            return {
                "id": id,
                "title": title,
                "uniqueSlug": uniqueSlug,
                "webCanonicalUrl": webCanonicalUrl,
                "audioVersionUrl": audioVersionUrl,
            }
        return {"message": "File not found"}
