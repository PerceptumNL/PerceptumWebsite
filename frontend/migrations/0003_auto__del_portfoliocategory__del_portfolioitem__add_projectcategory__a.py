# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'PortfolioCategory'
        db.delete_table(u'frontend_portfoliocategory')

        # Deleting model 'PortfolioItem'
        db.delete_table(u'frontend_portfolioitem')

        # Removing M2M table for field categories on 'PortfolioItem'
        db.delete_table(db.shorten_name(u'frontend_portfolioitem_categories'))

        # Adding model 'ProjectCategory'
        db.create_table(u'frontend_projectcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'frontend', ['ProjectCategory'])

        # Adding model 'Project'
        db.create_table(u'frontend_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=255, blank=True)),
            ('repository', self.gf('django.db.models.fields.URLField')(max_length=255, blank=True)),
            ('small_img', self.gf('django.db.models.fields.URLField')(max_length=255)),
            ('large_img', self.gf('django.db.models.fields.URLField')(max_length=255)),
        ))
        db.send_create_signal(u'frontend', ['Project'])

        # Adding M2M table for field categories on 'Project'
        m2m_table_name = db.shorten_name(u'frontend_project_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'frontend.project'], null=False)),
            ('projectcategory', models.ForeignKey(orm[u'frontend.projectcategory'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'projectcategory_id'])


    def backwards(self, orm):
        # Adding model 'PortfolioCategory'
        db.create_table(u'frontend_portfoliocategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'frontend', ['PortfolioCategory'])

        # Adding model 'PortfolioItem'
        db.create_table(u'frontend_portfolioitem', (
            ('website', self.gf('django.db.models.fields.URLField')(max_length=255, blank=True)),
            ('small_img', self.gf('django.db.models.fields.URLField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('repository', self.gf('django.db.models.fields.URLField')(max_length=255, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('large_img', self.gf('django.db.models.fields.URLField')(max_length=255)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'frontend', ['PortfolioItem'])

        # Adding M2M table for field categories on 'PortfolioItem'
        m2m_table_name = db.shorten_name(u'frontend_portfolioitem_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('portfolioitem', models.ForeignKey(orm[u'frontend.portfolioitem'], null=False)),
            ('portfoliocategory', models.ForeignKey(orm[u'frontend.portfoliocategory'], null=False))
        ))
        db.create_unique(m2m_table_name, ['portfolioitem_id', 'portfoliocategory_id'])

        # Deleting model 'ProjectCategory'
        db.delete_table(u'frontend_projectcategory')

        # Deleting model 'Project'
        db.delete_table(u'frontend_project')

        # Removing M2M table for field categories on 'Project'
        db.delete_table(db.shorten_name(u'frontend_project_categories'))


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
            'projects': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['frontend.Project']", 'symmetrical': 'False', 'blank': 'True'}),
            'tagline': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'twitter': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            'youtube': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'frontend.project': {
            'Meta': {'object_name': 'Project'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['frontend.ProjectCategory']", 'symmetrical': 'False', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'large_img': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'repository': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            'small_img': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'frontend.projectcategory': {
            'Meta': {'object_name': 'ProjectCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['frontend']