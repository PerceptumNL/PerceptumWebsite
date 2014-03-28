# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PortfolioItem'
        db.create_table(u'frontend_portfolioitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=255, blank=True)),
            ('repository', self.gf('django.db.models.fields.URLField')(max_length=255, blank=True)),
            ('small_img', self.gf('django.db.models.fields.URLField')(max_length=255)),
            ('large_img', self.gf('django.db.models.fields.URLField')(max_length=255)),
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

        # Adding model 'PortfolioCategory'
        db.create_table(u'frontend_portfoliocategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'frontend', ['PortfolioCategory'])


    def backwards(self, orm):
        # Deleting model 'PortfolioItem'
        db.delete_table(u'frontend_portfolioitem')

        # Removing M2M table for field categories on 'PortfolioItem'
        db.delete_table(db.shorten_name(u'frontend_portfolioitem_categories'))

        # Deleting model 'PortfolioCategory'
        db.delete_table(u'frontend_portfoliocategory')


    models = {
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