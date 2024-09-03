Unit Stati;

const MAXSIZE = 10;

type  Stat = record
       date: array[1..MAXSIZE] of integer;
       head, tail: integer;
     end;
     
procedure PushStatic( var Q: Stat; x: integer);
begin
  if Q.head = (Q.tail+1) mod MAXSIZE + 1 then 
  begin
    writeln('Очередь переполнена.');
    writeln('');
    Exit; 
  end;
  Q.tail := Q.tail mod MAXSIZE + 1;
  Q.date[Q.tail] := x;
end;

procedure PopStatic ( var Q: Stat);
begin
  if Q.head = Q.tail mod MAXSIZE + 1 then begin
    writeln('Очередь пуста.');
    writeln('');
    Exit;
  end;
  Q.date[Q.head]:= 0;
  Q.head := Q.head mod MAXSIZE + 1;
  writeln('Число удалено из начала очереди.');
  writeln('');
end;

begin
  
end.