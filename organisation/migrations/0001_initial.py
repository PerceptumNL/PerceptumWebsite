# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Member'
        db.create_table(u'organisation_member', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('tagline', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('img', self.gf('django.db.models.fields.URLField')(max_length=255)),
            ('facebook', self.gf('django.db.models.fields.URLField')(max_length=255, blank=True)),
            ('twitter', self.gf('django.db.models.fields.URLField')(max_length=255, blank=True)),
            ('linkedin', self.gf('django.db.models.fields.URLField')(max_length=255, blank=True)),
            ('youtube', self.gf('django.db.models.fields.URLField')(max_length=255, blank=True)),
            ('pinterest', self.gf('django.db.models.fields.URLField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'organisation', ['Member'])

        # Adding M2M table for field projects on 'Member'
        m2m_table_name = db.shorten_name(u'organisation_member_projects')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('member', models.ForeignKey(orm[u'organisation.member'], null=False)),
            ('project', models.ForeignKey(orm[u'organisation.project'], null=False))
        ))
        db.create_unique(m2m_table_name, ['member_id', 'project_id'])

        # Adding model 'Project'
        db.create_table(u'organisation_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=255, blank=True)),
            ('repository', self.gf('django.db.models.fields.URLField')(max_length=255, blank=True)),
            ('small_img', self.gf('django.db.models.fields.URLField')(max_length=255)),
            ('large_img', self.gf('django.db.models.fields.URLField')(max_length=255)),
        ))
        db.send_create_signal(u'organisation', ['Project'])

        # Adding M2M table for field categories on 'Project'
        m2m_table_name = db.shorten_name(u'organisation_project_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'organisation.project'], null=False)),
            ('projectcategory', models.ForeignKey(orm[u'organisation.projectcategory'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'projectcategory_id'])

        # Adding model 'ProjectCategory'
        db.create_table(u'organisation_projectcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'organisation', ['ProjectCategory'])


    def backwards(self, orm):
        # Deleting model 'Member'
        db.delete_table(u'organisation_member')

        # Removing M2M table for field projects on 'Member'
        db.delete_table(db.shorten_name(u'organisation_member_projects'))

        # Deleting model 'Project'
        db.delete_table(u'organisation_project')

        # Removing M2M table for field categories on 'Project'
        db.delete_table(db.shorten_name(u'organisation_project_categories'))

        # Deleting model 'ProjectCategory'
        db.delete_table(u'organisation_projectcategory')


    models = {
        u'organisation.member': {
            'Meta': {'object_name': 'Member'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'facebook': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'linkedin': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pinterest': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            'projects': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'members'", 'blank': 'True', 'to': u"orm['organisation.Project']"}),
            'tagline': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'twitter': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            'youtube': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'organisation.project': {
            'Meta': {'object_name': 'Project'},
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['organisation']