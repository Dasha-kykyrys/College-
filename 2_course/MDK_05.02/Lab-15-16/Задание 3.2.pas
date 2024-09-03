Program lab15;

type
  PNode = ^Node;
  Node = record
    element: integer;
    next: PNode;
  end;

var
  Head, p: PNode;
  i: integer;

function CreateNode(NewEl: integer): PNode;
var
  NewNode: PNode;
begin
  New(NewNode);
  NewNode^.element := NewEl;
  NewNode^.next := nil;
  Result := NewNode;
end;

procedure AddAfter(var p: PNode; NewNode: PNode);
begin
  NewNode^.next := p^.next;
  p^.next := NewNode;
end;

procedure AddFirst(var Head: PNode; NewNode: PNode);
begin
  NewNode^.next := Head;
  Head := NewNode;
end;

begin
  Head := nil;
  randomize;
  AddFirst(Head, CreateNode(random(1, 10)));
  p:= Head;
  for i := 1 to 9 do
  begin
     AddAfter(p, CreateNode(random(1, 10)));
      p:= p^.next;
  end;
  
  p := Head; 
  write('Список элементов: ');
  while p <> nil do
  begin
    write( p^.element, ' ');
    p := p^.next;        
  end;
  writeln();
  p := Head; 
  write('Чётные элементы: ');
  while p <> nil do
  begin
    if p^.element mod 2 = 0 then
        write( p^.element, ' ');
    p := p^.next;   
  end;
end.