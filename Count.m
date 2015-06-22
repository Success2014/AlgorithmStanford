% counte inversion
function [nArray c] = Count(array)

n = length(array);

if (n == 0) || (n == 1)
    c = 0;
    nArray = array;
else
    m = floor(n/2);
    F = array( 1 : m);
    S = array( m + 1 : end);
    
    [tmpa x] = Count(F);
    array(1 : m) = tmpa;
    
	[tmpb y] = Count(S);
    array( m + 1 : end) = tmpb;
    
	[nArray z] = CountSplitInv(array);
    c = x + y + z;
end