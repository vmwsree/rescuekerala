# -*- coding: utf-8 -*-
# @Author: Vivek Mohan
# @Date:   2018-08-16 18:27:34
# @Last Modified by:   Vivek Mohan
# @Last Modified time: 2018-08-16 18:34:48

import graphene

import mainapp.schema


class Query(mainapp.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


schema = graphene.Schema(query=Query)
