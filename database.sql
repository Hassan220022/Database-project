create database libManagement
use libManagement

create table Author(
authorID varchar(15),
authorName varchar(30),
primary key(authorID)
)

create table _Member(
memberID varchar(15),
memberName varchar(30),
primary key(memberID)
);
create table Staff(
staffID varchar(15),
staffName vadrchar(30),
primary key(staffID)
);
create table Book(
ISBN varchar(15) primary key,
title varchar(30),
authorID varchar(15) FOREIGN KEY REFERENCES Author(authorID),
staffID varchar(15) foreign key(staffID) references Staff,
);
create table Borrow(
borrowID varchar(15),
duedate date,
memberID varchar(15) not null,
ISBN varchar(15) not null,
primary key(borrowID),
foreign key(memberID) references _Member,
foreign key(ISBN) references Book
);
alter table Book alter column authorID varchar(15) not null
alter table Book alter column staffID varchar(15) not null

insert into Author(authorID,authorName) values('1','Shakespere')
insert into Author(authorID,authorName) values('2','JK Rowling')
insert into Author(authorID,authorName) values('3','Aghatha Christie')
insert into Author(authorID,authorName) values('4','Barbara Cartland')
insert into Author(authorID,authorName) values('5','Danielle Steel')
insert into Author(authorID,authorName) values('6','Harold Robbins')
insert into Author(authorID,authorName) values('7','Georges Simenon')
insert into Author(authorID,authorName) values('8','Enid Blyton')
insert into Author(authorID,authorName) values('9','Sidney Sheldon')
insert into Author(authorID,authorName) values('10','Eiichiro Oda')


insert into _Member(memberID,memberName) values('ammar123','Ammar Amin')
insert into _Member(memberID,memberName) values('mostafa73@','Mostafa Ahmed')
insert into _Member(memberID,memberName) values('3','Omar Ahmed')
insert into _Member(memberID,memberName) values('4','Youssef Sameh')
insert into _Member(memberID,memberName) values('5','Fekry Nabil')
insert into _Member(memberID,memberName) values('6','Amr Mohamed')
insert into _Member(memberID,memberName) values('7','George Mostafa')
insert into _Member(memberID,memberName) values('8','Reda Moussa')
insert into _Member(memberID,memberName) values('9','Osama Ahmed')
insert into _Member(memberID,memberName) values('10','Salah Kamel')

insert into Staff(staffID,staffName) values('123','Demi McIntyre')
insert into Staff(staffID,staffName) values('4892r','Eliseo Rojas')
insert into Staff(staffID,staffName) values('d43j4','Adaline Hendricks')
insert into Staff(staffID,staffName) values('rft5','Dash Leon')
insert into Staff(staffID,staffName) values('eof','Amora Barnett')
insert into Staff(staffID,staffName) values('rim8','Stephen Sofo')
insert into Staff(staffID,staffName) values('rmf4','Brynlee Wiley')
insert into Staff(staffID,staffName) values('jfu5','Mathew Christensen')
insert into Staff(staffID,staffName) values('fj8','Larmen Mata')
insert into Staff(staffID,staffName) values('fp0','Ray Faulkner')

insert into Book (ISBN,title,authorID,staffID) values('9r8f','Moby Dick','6','123')
insert into Book (ISBN,title,authorID,staffID) values('gtkm',' Anna Karenina','8','123')
insert into Book (ISBN,title,authorID,staffID) values('oogto',' Madame Bovary','6','123')
insert into Book (ISBN,title,authorID,staffID) values('pdfgr','War and Peace','6','rft5')
insert into Book (ISBN,title,authorID,staffID) values('4545','The Great Gatsby','6','123')
insert into Book (ISBN,title,authorID,staffID) values('4433','Lolita','6','123')
insert into Book (ISBN,title,authorID,staffID) values('2233','Middlemarch','4','eof')
insert into Book (ISBN,title,authorID,staffID) values('1122','Naruto','6','123')
insert into Book (ISBN,title,authorID,staffID) values('0405','Monster','6','123')
insert into Book (ISBN,title,authorID,staffID) values('3549','Berserk','6','123')
select * from Book
