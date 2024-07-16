#!/usr/bin/env python3
""" List all documents in Python."""
from pymongo import MongoClient


def list_all(mongo_collection):
    """Return an empty list if no document in the collection"""
    documents = mongo_collection.find()
    return [doc for doc in documents]
