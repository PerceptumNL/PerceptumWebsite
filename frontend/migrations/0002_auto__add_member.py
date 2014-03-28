# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Member'
        db.create_table(u'frontend_member', (
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
        db.send_create_signal(u'frontend', ['Member'])

        # Adding M2M table for field projects on 'Member'
        m2m_table_name = db.shorten_name(u'frontend_member_projects')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('member', models.ForeignKey(orm[u'frontend.member'], null=False)),
            ('portfolioitem', models.ForeignKey(orm[u'frontend.portfolioitem'], null=False))
        ))
        db.create_unique(m2m_table_name, ['member_id', 'portfolioitem_id'])


    def backwards(self, orm):
        # Deleting model 'Member'
        db.delete_table(u'frontend_member')

        # Removing M2M table for field projects on 'Member'
        db.delete_table(db.shorten_name(u'frontend_member_projects'))


    models = {
        u'frontend.member': {
            'Meta': {'object_name': 'Member'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'facebook': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'linkedin': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pinterest': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            'projects': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['frontend.PortfolioItem']", 'symmetrical': 'False', 'blank': 'True'}),
            'tagline': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'twitter': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            'youtube': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'frontend.portfoliocategory': {
            'Meta': {'object_name': 'PortfolioCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'frontend.portfolioitem': {
            'Meta': {'object_name': 'PortfolioItem'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['frontend.PortfolioCategory']", 'symmetrical': 'False', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'large_img': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'repository': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            'small_img': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['frontend']