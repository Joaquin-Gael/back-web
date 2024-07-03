--query 1
select concat(d.nombre, ' ', d.apellido), m.nombre_mascota, b.nombre from dueños as d 
inner join barrios as b on d.id_barrio = b.id_barrio 
inner join mascotas as m on m.id_dueño = d.id_dueño
order by d.id_dueño

--query 2
select m.nombre_mascota, concat(d.nombre,' ',d.apellido) from mascotas as m
inner join dueños as d on m.id_dueño = d.id_dueño

--query 3
select d.email,b.nombre,m.id_mascota from dueños as d
join barrios as b on d.id_barrio = b.id_barrio 
join mascotas as m on d.id_dueño = m.id_dueño

--query 4 
select concat(d.nombre,' ',d.apellido),m.nombre_mascota from mascotas as m
join dueños as d on m.nombre_mascota = 'Conejito' and m.id_dueño = d.id_dueño

--query 5 
select d.telefono, d.email from dueños as d
join mascotas as m on d.id_dueño = m.id_dueño and m.raza = 'Holandés Enano'

--query 6
select extract(year from m.fecha_nacim) as año_nacim, d.* from mascotas as m 
join dueños as d on m.id_dueño = d.id_dueño and extract(year from m.fecha_nacim) = '2022'

--query 7
select m.nombre_mascota, m.tipo, concat(d.nombre, ' ', d.apellido)as nombre_completo, d.email from mascotas as m 
join dueños as d on m.id_dueño = d.id_dueño and m.descripcion like '%color%'

--query 8
select concat(d.nombre, ' ', d.apellido), b.nombre as Nombre from dueños as d
join barrios as b on not b.nombre like '%centro%' and d.id_barrio = b.id_barrio and d.telefono like '%8'

--query 9
select m.nombre_mascota, concat(d.nombre, ' ', d.apellido)as Nombre_dueño from mascotas as m
join dueños as d on m.id_dueño = d.id_dueño and extract(month from m.fecha_nacim) between 1 and 7

--query 10
select d.telefono, b.nombre from dueños as d
join barrios as b on d.id_barrio = b.id_barrio
join mascotas as m on d.id_dueño = m.id_dueño and m.tipo = 'Doméstico'
order by m.fecha_nacim desc

--query 11-12
create table turnos(
	nro_turno serial primary key,
	fecha_turno date not null,
	precio_consulta float,
	id_mascota integer,
	motivo varchar(100),
    FOREIGN KEY (id_mascota) REFERENCES mascotas(id_mascota)
);
insert into turnos (fecha_turno,precio_consulta,id_mascota,motivo) values
('2023-08-02', 3500, 2, 'le faltan vacunas'),
('2023-09-15', 3600, 3, 'tenia pulgas asique se lo bañó'),
('2023-09-15', 2600, 4, 'preguntaron por la comida y sus cuidados'),
('2023-09-20', 4000, 5, 'se quebró el pico, lo curamos y lo desempulgamos'),
('2023-09-22', 4500, 6, 'vacunas y baño'),
('2023-08-21', 2600, 7, 'vino por una herida en el caparazón'),
('2023-08-30', 4000, 8, 'mucha comida, dolor de panza'),
('2022-11-16', 4500, 2, 'está preñada. vino a control'),
('2022-11-17', 4000, 3, 'dolor de oídos. receto gotitas'),
('2022-10-19', 2600, 4, 'tuvieron cria.'),
('2022-10-22', 3600, 5, 'se voló y se golpeó!'),
('2022-10-25', 4500, 6, 'preñada!! vacunas y desparasitarla'),
('2022-09-22', 2600, 7, 'control de golpe anterior'),
('2022-09-20', 4500, 8, 'llevo comida y semillas, haciendo dieta sana con verduras por malestar de panza');
select * from turnos;

--query 13
select t.nro_turno, m.nombre_mascota, concat(d.nombre, ' ', d.apellido)as Nombre_dueño from turnos as t
join mascotas as m on t.id_mascota = m.id_mascota and extract(year from t.fecha_turno) = '2023'
join dueños as d on m.id_dueño = d.id_dueño

--query 14
select t.fecha_turno, m.nombre_mascota, concat(d.nombre, ' ', d.apellido) from turnos as t
join mascotas as m on t.id_mascota = m.id_mascota and t.motivo like '%vacunas%'
join dueños as d on m.id_dueño = d.id_dueño

--query 15
select t.fecha_turno, t.motivo from turnos as t
join mascotas as m on t.id_mascota = m.id_mascota and extract(year from t.fecha_turno) = '2022'

--query 16
select m.