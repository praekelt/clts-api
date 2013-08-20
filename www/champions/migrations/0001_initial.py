# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CommunityChampion'
        db.create_table(u'champions_communitychampion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('msisdn', self.gf('django.db.models.fields.CharField')(max_length=18)),
        ))
        db.send_create_signal(u'champions', ['CommunityChampion'])

        # Adding model 'Activation'
        db.create_table(u'champions_activation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entered', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('matched', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['champions.CommunityChampion'])),
            ('activation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'champions', ['Activation'])


    def backwards(self, orm):
        # Deleting model 'CommunityChampion'
        db.delete_table(u'champions_communitychampion')

        # Deleting model 'Activation'
        db.delete_table(u'champions_activation')


    models = {
        u'champions.activation': {
            'Meta': {'object_name': 'Activation'},
            'activation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'entered': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'matched': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['champions.CommunityChampion']"})
        },
        u'champions.communitychampion': {
            'Meta': {'object_name': 'CommunityChampion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'msisdn': ('django.db.models.fields.CharField', [], {'max_length': '18'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['champions']