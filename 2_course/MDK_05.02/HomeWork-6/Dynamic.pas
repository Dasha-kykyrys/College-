Unit Dynamic;

type PNode = ^Node;
     Node = record
       data: integer;
       next: PNode;
     end;
     Dyinamic = record
       head, tail: PNode;
     end;

procedure PushDynamic( var Q: Dyinamic; x: integer );
var NewNode: PNode;
begin
  New(NewNode);
  NewNode^.data := x;
  NewNode^.next := nil;
  if Q.tail <> nil then
    Q.tail^.next := NewNode;
  Q.tail := NewNode; 
  if Q.head = nil then Q.head := Q.tail;
end;

procedure PopDynamic ( var Q: Dyinamic );
var top: PNode;
begin
  if Q.head = nil then begin
    writeln('Очередь пуста.');
    writeln('');
    Exit;
  end;
  top := Q.head;
  Q.head := top^.next;
  if Q.head = nil then Q.tail := nil;
  writeln('Число удалено из начала очереди.');
  writeln('');
  Dispose(top);
end;


begin
  
end.