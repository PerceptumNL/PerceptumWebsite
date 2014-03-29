# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Member.email'
        db.add_column(u'organisation_member', 'email',
                      self.gf('django.db.models.fields.EmailField')(default='', max_length=255, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Member.email'
        db.delete_column(u'organisation_member', 'email')


    models = {
        u'organisation.member': {
            'Meta': {'object_name': 'Member'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            'linkedin': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pinterest': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            'projects': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'members'", 'blank': 'True', 'to': u"orm['organisation.Project']"}),
            'tagline': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            'youtube': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'organisation.organisation': {
            'Meta': {'object_name': 'Organisation'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'facebook': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'linkedin': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            'logo': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'pinterest': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            'slogan': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'tagline': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'timezone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            'youtube': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'organisation.project': {
            'Meta': {'object_name': 'Project'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['organisation.ProjectCategory']", 'symmetrical': 'False', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'large_img': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'repository': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            'small_img': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'organisation.projectcategory': {
            'Meta': {'object_name': 'ProjectCategory'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['organisation']