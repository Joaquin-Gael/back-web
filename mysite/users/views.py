from django.shortcuts import render
from django.views import View
from django.utils import timezone
from django.contrib.auth import (authenticate, login, logout)
from rest_framework import (viewsets, views, permissions, status, response)
from . import (serializers, models)

# Create your views here.

class UserViews(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.AllowAny]

class TypeUserViews(viewsets.ModelViewSet):
    queryset = models.TypeUser.objects.all()
    serializer_class = serializers.TypeUserSerializer
    permission_classes = [permissions.AllowAny]

class VisitCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        try:
            ip_addres = request.META.get('REMOTE_ADDR')
            user_agent = request.META.get('HTTP_USER_AGENT','')
            models.Visit.objects.create(
                timestap=timezone.now(),
                ip_addres=ip_addres,
                user_agent=user_agent
            )
            serializer = serializers.VisitSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                self.update_weekly_visit_count()
                return response.Response(serializer.data, status=status.HTTP_201_CREATED)
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            print(f'Error: {err}')
            return response.Response({'message':'Error data no presentada'},status=status.HTTP_400_BAD_REQUEST)
    
    def update_weekly_visit_count(self):
        now = timezone.now()
        start_of_week = now - timedelta(days=now.weekday())
        end_of_week = start_of_week + timedelta(days=6)

        weekly_visit, created = models.Visit.objects.get_or_create(
            timestap__gte=start_of_week,
            timestap__lte=end_of_week,
            default = {'visit_count': 0}
        )

        weekly_visit.visit_count += 1
        weekly_visit.save()


class VisitDataChart(views.APIView):
    def get(self,request,*args,**kwargs):
        try:
            categories, data = self.get_weekly_visit_data()
            chart_data = {
                'tooltip':{
                    'show':True,
                    'trigger':'axis',
                    'axisPointer': {
                        'type': 'cross',
                        'label': {
                            'backgroundColor': '#6a7985'
                        }
                    }
                },
                'xAxis': {
                    'type': 'category',
                    'boundaryGap': False,
                    'data': categories,
                },
                'yAxis': {
                    'type': 'value',
                },
                'series': [
                    {
                        'data': data,
                        'type': 'line',
                        'areaStyle': {},
                    }
                ]
            }
            return response.Response(chart_data,status=status.HTTP_200_OK)
        except Exception as err:
            print(f'Error en el chart: {err}')
            return response.Response({'message':f'Error {err}'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def get_weekly_visit_data(self):
        try:
            weekly_visits = models.WeeklyVisit.objects.all().order_by('week_start')

            categories = []
            data = []

            for visit in weekly_visits:
                categories.append(visit.week_start.strftime('%a'))
                data.append(visit.visit_count if visit.visit_count else 0)
            
            return categories, data
        except Exception as err:
            print(f'Error en get visit: {err}')
            return response.Response({'message':f'Error {err}'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
