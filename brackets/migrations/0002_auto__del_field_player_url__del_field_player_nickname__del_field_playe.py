# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Player.url'
        db.delete_column('brackets_player', 'url')

        # Deleting field 'Player.nickname'
        db.delete_column('brackets_player', 'nickname')

        # Deleting field 'Player.slug'
        db.delete_column('brackets_player', 'slug')

        # Adding field 'Player.tournament'
        db.add_column('brackets_player', 'tournament',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['brackets.Tournament']),
                      keep_default=False)

    def backwards(self, orm):
        # Adding field 'Player.url'
        db.add_column('brackets_player', 'url',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Player.nickname'
        raise RuntimeError("Cannot reverse this migration. 'Player.nickname' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Player.slug'
        raise RuntimeError("Cannot reverse this migration. 'Player.slug' and its values cannot be restored.")
        # Deleting field 'Player.tournament'
        db.delete_column('brackets_player', 'tournament_id')

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'brackets.bracket': {
            'Meta': {'ordering': "['tournament', 'order']", 'unique_together': "(['tournament', 'slug', 'order'],)", 'object_name': 'Bracket'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'tournament': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'brackets'", 'to': "orm['brackets.Tournament']"})
        },
        'brackets.match': {
            'Meta': {'ordering': "['the_round', 'order']", 'object_name': 'Match'},
            'end_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'outcome': ('django.db.models.fields.CharField', [], {'default': "'unplayed'", 'max_length': '32'}),
            'player_1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'matches_1'", 'to': "orm['brackets.Player']"}),
            'player_1_score': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'blank': 'True'}),
            'player_2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'matches_2'", 'to': "orm['brackets.Player']"}),
            'player_2_score': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'the_round': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'matches'", 'to': "orm['brackets.Round']"}),
            'winner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'matches_won'", 'null': 'True', 'to': "orm['brackets.Player']"})
        },
        'brackets.player': {
            'Meta': {'ordering': "['player']", 'object_name': 'Player'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'league': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '64', 'blank': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tournament_profile'", 'to': "orm['auth.User']"}),
            'rank': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'seed': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'tournament': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['brackets.Tournament']"})
        },
        'brackets.round': {
            'Meta': {'ordering': "['bracket', 'slug', 'order']", 'object_name': 'Round'},
            'bracket': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rounds'", 'to': "orm['brackets.Bracket']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'brackets.tournament': {
            'Meta': {'ordering': "['-start_date', 'name']", 'object_name': 'Tournament'},
            'end_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['brackets']
