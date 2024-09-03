Unit Fractal1;
uses GraphABC;
Procedure Draw(x, y, x1, y1: Real; depth: Integer);
var
   xn, yn, x1n, y1n: Real;
begin
     if  depth = 0  Then
       Exit
     else
     begin
          xn := 2*x/3 + x1 / 3;
          x1n := x/3 + 2*x1 / 3;
          yn := 2*y/3 + y1 / 3;
          y1n := y/3 + 2*y1 / 3;
          Rectangle(Round(xn), Round(yn), Round(x1n), Round(y1n));
          Draw(x, y, xn, yn, depth-1);
          Draw(xn, y, x1n, yn, depth-1);
          Draw(x1n, y, x1, yn, depth-1);
          Draw(x, yn, xn, y1n, depth-1);
          Draw(x1n, yn, x1, y1n, depth-1);
          Draw(x, y1n, xn, y1, depth-1);
          Draw(xn, y1n, x1n, y1, depth-1);
          Draw(x1n, y1n, x1, y1, depth-1);
     end
end;
begin
  
end.
