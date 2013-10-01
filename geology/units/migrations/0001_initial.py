# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Unit'
        db.create_table(u'units_unit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.GeometryField')()),
        ))
        db.send_create_signal(u'units', ['Unit'])


    def backwards(self, orm):
        # Deleting model 'Unit'
        db.delete_table(u'units_unit')


    models = {
        u'units.unit': {
            'Meta': {'object_name': 'Unit'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'geom': ('django.contrib.gis.db.models.fields.GeometryField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        }
    }

    complete_apps = ['units']