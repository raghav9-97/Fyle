from tastypie.resources import ModelResource
from api.models import Branches
from django.db.models import Q

class BranchResource(ModelResource):
    def build_filters(self, filters=None):
        if filters is None:
            filters = {}
        orm_filters = super(BranchResource, self).build_filters(filters)

        if 'q' in filters:
            query = filters['q']
            orm_filters['branch__icontains'] = filters['q']
        
        return orm_filters

    class Meta:
        queryset = Branches.objects.all().order_by('ifsc')
        resource_name = 'branches/autocomplete'
        include_resource_uri = False

class SearchResource(ModelResource):
    def build_filters(self, filters=None):
        if filters is None:
            filters = {}
        orm_filters = super(SearchResource, self).build_filters(filters)

        if 'q' in filters:
            query = filters['q']
            qset = (
                    Q(ifsc__icontains=query) |
                    Q(bank_id__icontains=query) |
                    Q(branch__icontains=query) | Q(address__icontains=query) | Q(city__icontains=query) |
                    Q(district__icontains=query) | Q(state__icontains=query) )
            orm_filters.update({'custom': qset})

        return orm_filters

    def apply_filters(self, request, applicable_filters):
        if 'custom' in applicable_filters:
            custom = applicable_filters.pop('custom')
        else:
            custom = None

        semi_filtered = super(SearchResource, self).apply_filters(request, applicable_filters)

        return semi_filtered.filter(custom) if custom else semi_filtered

    class Meta:
        queryset = Branches.objects.all().order_by('ifsc')
        resource_name = 'branches'
        include_resource_uri = False
