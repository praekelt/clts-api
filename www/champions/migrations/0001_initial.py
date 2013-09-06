# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Champion'
        db.create_table(u'champions_champion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('msisdn', self.gf('django.db.models.fields.CharField')(unique=True, max_length=18)),
            ('activated', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('activation_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'champions', ['Champion'])

        # Adding model 'Village'
        db.create_table(u'champions_village', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('champion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['champions.Champion'])),
            ('latitude', self.gf('django.db.models.fields.CharField')(max_length=16, blank=True)),
            ('longitude', self.gf('django.db.models.fields.CharField')(max_length=16, blank=True)),
        ))
        db.send_create_signal(u'champions', ['Village'])


    def backwards(self, orm):
        # Deleting model 'Champion'
        db.delete_table(u'champions_champion')

        # Deleting model 'Village'
        db.delete_table(u'champions_village')


    models = {
        u'champions.champion': {
            'Meta': {'object_name': 'Champion'},
            'activated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'activation_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'msisdn': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '18'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'champions.village': {
            'Meta': {'object_name': 'Village'},
            'champion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['champions.Champion']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['champions']