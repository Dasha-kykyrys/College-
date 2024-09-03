Program Queue;
uses Crt, Stati, Dynamic;

 var n: integer;  
 QS: Stat;
 QD:Dyinamic;

 procedure Statik;
 var  f, i: integer;
 begin
   writeln('1 - Добавить число.');
   writeln('2 - Удалить число.');
   writeln('3 - Вывод содержимого очереди.');
   writeln('4 - Выход из программы.');
   writeln('5 - Смена типа памяти.');
   readln(n);
   case n of
     1:begin ClrScr; write('Введите число: '); readln(f); ClrScr; PushStatic(QS, f); end;
     2:begin ClrScr; PopStatic(QS); writeln(''); end;
     3:begin ClrScr; write('Очередь: '); for i:=1 to MAXSIZE do write(QS.date[i], ' '); writeln(''); writeln(''); end;
   end;
 end;
 
 procedure Dynamik;
  var  f: integer;
  top: PNode;
 begin
   writeln('1 - Добавить число.');
   writeln('2 - Удалить число.');
   writeln('3 - Вывод содержимого очереди.');
   writeln('4 - Выход из программы.');
   writeln('5 - Смена типа памяти.');
   readln(n);
   top := QD.head;
      case n of
     1:begin ClrScr; write('Введите число: '); readln(f); ClrScr; PushDynamic(QD, f); end;
     2:begin ClrScr;  PopDynamic(QD); end;
     3:begin ClrScr; write('Очередь: '); while top <> nil do begin write(top^.data, ' '); top := top^.next; end; writeln(' '); writeln(''); end;
 end;
 end;
 
 
procedure Clean ( var Q: Dyinamic );
var top: PNode;
begin
  if Q.head = nil then begin
    Exit;
  end;
  top := Q.head;
  Q.head := top^.next;
  if Q.head = nil then Q.tail := nil;
  Dispose(top);
end;
 
 procedure Start();
 var i:integer;
 begin
  ClrScr();
  n:= 0;
  writeln('Выберите тип памяти. ');
  writeln('1 - Динамическая память.');
  writeln('2 - Статическая память.'); 
  QS.head:= 1;
  QS.tail:= 0;
  QD.head:= nil;
  QD.tail:= nil;
  readln(n);
  case n of
    1:begin ClrScr; while (n <> 4) do begin Dynamik; if n = 5 then begin  while QD.head <> nil do begin Clean(QD); end; Start();  end; end; end;
    2:begin ClrScr; while (n <> 4) do begin Statik; if n = 5 then begin for i:=1 to MAXSIZE do QS.date[i]:=0; Start(); end; end; end;
  end;  
 end;
 
begin
 Start();
end.