# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Proyectos'
        db.create_table('registros_proyectos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('proyecto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['proyectos_academicos.Proyecto'])),
            ('voluntario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['proyectos_academicos.Voluntario'])),
            ('horas', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('fecha', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('actividad', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('registros', ['Proyectos'])

        # Adding model 'Servicios'
        db.create_table('registros_servicios', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('servicio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['proyectos_academicos.Servicio'])),
            ('voluntario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['proyectos_academicos.Voluntario'])),
            ('horas', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('fecha', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('actividad', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('registros', ['Servicios'])


    def backwards(self, orm):
        # Deleting model 'Proyectos'
        db.delete_table('registros_proyectos')

        # Deleting model 'Servicios'
        db.delete_table('registros_servicios')


    models = {
        'proyectos_academicos.categoriasproyecto': {
            'Meta': {'object_name': 'CategoriasProyecto'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'proyectos_academicos.institucion': {
            'Meta': {'object_name': 'Institucion'},
            'coordinador': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'correo_electronico': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'nucleo': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'telefonos': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'proyectos_academicos.proyecto': {
            'Meta': {'object_name': 'Proyecto'},
            'categorias': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['proyectos_academicos.CategoriasProyecto']", 'null': 'True', 'blank': 'True'}),
            'dependencia': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'especialidad': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'estatus': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'tutor': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        },
        'proyectos_academicos.servicio': {
            'Meta': {'object_name': 'Servicio'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'servicio': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'turno': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'proyectos_academicos.voluntario': {
            'CI': ('django.db.models.fields.CharField', [], {'max_length': '10', 'primary_key': 'True'}),
            'Meta': {'object_name': 'Voluntario'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'correo_electronico': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'estado_civil': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {}),
            'genero': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'grado_instruccion': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'default': "'imagenes/ninguna.png'"}),
            'institucion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['proyectos_academicos.Institucion']"}),
            'lugar_nacimiento': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'ocupacion': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'primer_nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'telefono_casa': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'telefono_celular': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'registros.proyectos': {
            'Meta': {'object_name': 'Proyectos'},
            'actividad': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'horas': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'proyecto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['proyectos_academicos.Proyecto']"}),
            'voluntario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['proyectos_academicos.Voluntario']"})
        },
        'registros.servicios': {
            'Meta': {'object_name': 'Servicios'},
            'actividad': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'horas': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'servicio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['proyectos_academicos.Servicio']"}),
            'voluntario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['proyectos_academicos.Voluntario']"})
        }
    }

    complete_apps = ['registros']