program lab15;

type
  PNode = ^Node;
  Node = record
    element: string;
    next: PNode;
  end;

var
  Head, p: PNode;
  i, cnt: integer;
  F: Text;

function CreateNode(NewEl: string): PNode;
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

function TakeWord(F: Text): string;
var
  c: char;
begin
  Result := ''; 
  c := ' ';    
  while not eof(f) and (c <= ' ') do 
    read(F, c);  
  while not eof(f) and (c > ' ') do
  begin
    Result := Result + c;
    read(F, c);
  end;
end;

begin
  Assign(F, 'words2.txt');
  Reset(F);
  Head := nil;
  AddFirst(Head, CreateNode(TakeWord(F)));
  p:= Head;
  for i := 1 to 9 do
  begin
    AddAfter(p, CreateNode(TakeWord(F)));
      p:= p^.next;
  end;
  Close(F);
  
  p := Head; 
  write('Список: ');
  while p <> nil do
  begin
    write( p^.element, ' ');
    p := p^.next;        
  end;
  writeln();
  p := Head; 
  write('На чётных позициях: ');
  while p <> nil do
  begin
    cnt +=1;
    if cnt mod 2 = 0 then
        write( p^.element, ' ');
    p := p^.next;   
  end;
end.