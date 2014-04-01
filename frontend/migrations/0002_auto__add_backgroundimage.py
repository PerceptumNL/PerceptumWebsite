# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BackgroundImage'
        db.create_table(u'frontend_backgroundimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=255)),
            ('interface', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['frontend.Interface'])),
        ))
        db.send_create_signal(u'frontend', ['BackgroundImage'])


    def backwards(self, orm):
        # Deleting model 'BackgroundImage'
        db.delete_table(u'frontend_backgroundimage')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'frontend.backgroundimage': {
            'Meta': {'object_name': 'BackgroundImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interface': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['frontend.Interface']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255'})
        },
        u'frontend.interface': {
            'Meta': {'object_name': 'Interface'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page_description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'page_icon': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            'page_title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'polymorphic_frontend.interface_set'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'template': ('django.db.models.fields.CharField', [], {'default': "'index.html'", 'max_length': '255'})
        },
        u'frontend.trebleinterface': {
            'Meta': {'object_name': 'TrebleInterface', '_ormbases': [u'frontend.Interface']},
            'contact_intro': ('django.db.models.fields.TextField', [], {}),
            'contact_title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'description_title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ganalytics_id': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'interface_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['frontend.Interface']", 'unique': 'True', 'primary_key': 'True'}),
            'member_project_filter': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'members_intro': ('django.db.models.fields.TextField', [], {}),
            'members_title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'scrolldown_flipped_visual': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'scrolldown_visual': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'show_social': ('django.db.models.fields.BooleanField', [], {}),
            'work_intro': ('django.db.models.fields.TextField', [], {}),
            'work_title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['frontend']