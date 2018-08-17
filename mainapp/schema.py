# -*- coding: utf-8 -*-
# @Author: Vivek Mohan
# @Date:   2018-08-16 18:23:02
# @Last Modified by:   Vivek Mohan
# @Last Modified time: 2018-08-17 23:58:21
import graphene

from graphene_django import DjangoObjectType
from .models import Request, Volunteer, Contributor, DistrictCollection, DistrictManager,DistrictNeed, RescueCamp, Person
from graphene import relay, ObjectType


class RequestType(DjangoObjectType):
    class Meta:
        model = Request

class VolunteerType(DjangoObjectType):
    class Meta:
        model = Volunteer


class ContributorType(DjangoObjectType):
    class Meta:
        model = Contributor


class DistrictCollectionType(DjangoObjectType):
    class Meta:
        model = DistrictCollection


class DistrictManagerType(DjangoObjectType):
    class Meta:
        model = DistrictManager


class DistrictNeedType(DjangoObjectType):
    class Meta:
        model = DistrictNeed


class RescueCampType(DjangoObjectType):
    class Meta:
        model = RescueCamp


class PersonType(DjangoObjectType):
    class Meta:
        model = Person


class Query(graphene.AbstractType):
    requests = graphene.List(RequestType)
    volunteer = graphene.List(VolunteerType)
    contributor = graphene.List(ContributorType)
    districtCollection = graphene.List(DistrictCollectionType)
    districtManager = graphene.List(DistrictManagerType)
    districtNeed = graphene.List(DistrictNeedType)
    rescueCamp = graphene.List(RescueCampType)
    person = graphene.List(PersonType)
    filterRequests = graphene.List(RequestType,
                                   status_types=graphene.String(),
                                   district=graphene.String())

    def resolve_requests(self, info, **kwargs):
        return Request.objects.all()

    def resolve_volunteer(self, info, **kwargs):
        return Volunteer.objects.all()

    def resolve_contributor(self, info, **kwargs):
        return Contributor.objects.all()

    def resolve_districtCollection(self, info, **kwargs):
        return DistrictCollection.objects.all()

    def resolve_districtManager(self, info, **kwargs):
        return DistrictManager.objects.all()

    def resolve_districtNeed(self, info, **kwargs):
        return DistrictNeed.objects.all()

    def resolve_rescueCamp(self, info, **kwargs):
        return RescueCamp.objects.all()

    def resolve_person(self, info, **kwargs):
        return Person.objects.all()

    def resolve_filterRequests(self, info, **kwargs):
        status_types = kwargs.get('status_types')
        district = kwargs.get('district')

        if status_types is not None:
            return Request.objects.filter(status_types=status_types)
        if district is not None:
            return Request.objects.filter(district=district)
