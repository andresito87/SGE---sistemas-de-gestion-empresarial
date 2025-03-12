# -*- coding: utf-8 -*-

from odoo import models, fields, api # type: ignore

class biblioteca(models.Model):
    _name = 'moduloapg.biblioteca'
    _description= 'Permite definir las características de una biblioteca'

    name = fields.Char('Nombre')
    capacidad = fields.Integer('Capacidad')
    
    libros_ids=fields.One2many('moduloapg.libro','biblioteca_id',string='Libros')
    
class libro(models.Model):
    _name = 'moduloapg.libro'
    _description= 'Permite definir las características de un libro'

    name = fields.Char('Nombre')
    publicado = fields.Date('Fecha de publicación')
    precio = fields.Float('Precio',(4,1),default=0.0, help='P.V.P. del libro')
    genero = fields.Selection(string='genero',selection=[('f','Ficción'),('n','Novela'),('p','Poesía')],default='f')

    biblioteca_id = fields.Many2one('moduloapg.biblioteca', string='Biblioteca')
    autor_ids=fields.Many2many('moduloapg.autor', string='Autores')
    

class autor(models.Model):
    _name = 'moduloapg.autor'
    _description= 'Permite definir las características de un autor'

    name = fields.Char('Nombre')
    nacionalidad = fields.Char('Nacionalidad')
    
    libro_ids=fields.Many2many('moduloapg.libro', string='Libros')
