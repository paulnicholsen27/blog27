# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Post.author'
        db.add_column(u'blog_post', 'author',
                      self.gf('django.db.models.fields.CharField')(default='Paul Nichols', max_length=255),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Post.author'
        db.delete_column(u'blog_post', 'author')


    models = {
        u'blog.post': {
            'Meta': {'ordering': "['-created']", 'object_name': 'Post'},
            'author': ('django.db.models.fields.CharField', [], {'default': "'Paul Nichols'", 'max_length': '255'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['blog']