from dataclasses import fields
from rest_framework import serializers
from LMSapp.models import IB,RB,ABB,NAB



class IBSerializers(serializers.ModelSerializer):
    class Meta:
        model = IB
        fields =  ('Book_id','BookName','WriterName','stname','stemail','stdept','DateIssued')

class RBSerializers(serializers.ModelSerializer):
    class Meta:
        model = RB
        fields =  ('Book_id','BookName','WriterName','stname','stemail','stdept','Datereturned')

class ABBSerializers(serializers.ModelSerializer):
    class Meta:
        model = ABB
        fields =  ('Book_id','BookName','WriterName','stname','stemail','stdept','Dateretreived')

class NABSerializers(serializers.ModelSerializer):
    class Meta:
        model = NAB
        fields =  ('Book_id','BookName','WriterName','DateAdded')
