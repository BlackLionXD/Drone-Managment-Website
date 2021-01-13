from rest_framework import serializers
from .models import Transaction, FlightOperation, FlightPlan, FlightPermission, UINApplication
from registry.serializers import AircraftDetailSerializer, OperatorSelectRelatedSerializer



class UINApplicationSerializer(serializers.ModelSerializer):
    ''' A serializer forUIN '''
    drone = AircraftDetailSerializer(read_only=True)
    operator = OperatorSelectRelatedSerializer(read_only=True)
    class Meta:
        model = UINApplication
        fields = '__all__'		
        ordering = ['-created_at']
        
class FlightPlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = FlightPlan		
        fields = '__all__'
        ordering = ['-created_at']

class FlightOperationListSerializer(serializers.ModelSerializer):
    ''' A serializer for Flight Operations '''
    class Meta:
        model = FlightOperation	
        fields = ['id', 'name']
        ordering = ['-created_at']
    

 
class FlightOperationSerializer(serializers.ModelSerializer):
    ''' A serializer for Flight Operations '''
    drone = AircraftDetailSerializer(read_only=True)
    flight_plan = FlightPlanSerializer(read_only=True)
    class Meta:
        model = FlightOperation	
        fields = '__all__'	
        ordering = ['-created_at']
        
class FlightPermissionSerializer(serializers.ModelSerializer):
    operation = FlightOperationSerializer(read_only=True)
    class Meta:
        model = FlightPermission	
        fields = '__all__'	
        ordering = ['-created_at']
        
class TransactionSerializer(serializers.ModelSerializer):
    ''' A serializer to the transaction view '''

    class Meta:
        model = Transaction		
        fields = '__all__'
        ordering = ['-created_at']
