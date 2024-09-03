Program Fractal;
uses Fractal1, GraphABC;
var i, ws, ad, depth: integer;

Procedure Text();
begin
  TextOut(10, 10, 'Q - Увеличение фрактала.');
  TextOut(10, 30, 'E - Уменьшение фрактала.');
  TextOut(10, 50, 'W - Перемещение вверх.');
  TextOut(10, 70, 'A - Перемещение вправо.');
  TextOut(10, 90, 'S - Перемещение вниз.');
  TextOut(10, 110, 'D - Перемещение влево.');
  TextOut(10, 130, 'R - Увеличение глубины.');
  TextOut(10, 150, 'T - Уменьшение глубины.');
end;


Procedure KeyPress(key:integer);
begin
  case key of 
    VK_Q:begin i += 40;  end;
    VK_E:begin if i<>0 then begin i -= 40; end; end;
    
    VK_S:begin ws += 10; end;
    VK_W:begin ws -= 10; end;
    VK_D:begin ad += 10; end;
    VK_A:begin ad -= 10; end; 
    
    VK_R:begin if depth<6 then begin depth +=1; end; end;
    VK_T:begin if depth>1 then begin depth -=1; end; end;
  end;
  ClearWindow; 
  Text(); 
  Draw(220 + ad, 20 + ws, 240 + i + ad, 40 + i + ws, depth);
  redraw;
end;

begin
  i:= 0;
  ws:= 0;
  ad:= 0;
  depth:= 6;
  LockDrawing;
  Text();
  OnKeyDown:= KeyPress;
  Draw(220, 20, 240, 40, depth);
  redraw;
end.