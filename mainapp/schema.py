# -*- coding: utf-8 -*-
# @Author: Vivek Mohan
# @Date:   2018-08-16 18:23:02
# @Last Modified by:   Vivek Mohan
# @Last Modified time: 2018-08-16 18:50:15
import graphene
from graphene_django import DjangoObjectType
from .models import Request, Volunteer, Contributor, DistrictCollection, DistrictManager, DistrictNeed
from graphene import relay


class RequestType(DjangoObjectType):
    class Meta:
        model = Request


class Query(graphene.AbstractType):
    requests = graphene.List(RequestType)
    filterRequests = graphene.List(RequestType,
                                   status_types=graphene.String(),
                                   district=graphene.String())

    def resolve_requests(self, info, **kwargs):
        return Request.objects.all()

    def resolve_filterRequests(self, info, **kwargs):
        status_types = kwargs.get('status_types')
        district = kwargs.get('district')

        if status_types is not None:
            return Request.objects.filter(status_types=status_types)
        if district is not None:
            return Request.objects.filter(district=district)
