% count split inversion
function [nArray c] = CountSplitInv(array)

c = 0;
n = length(array);
m = floor(n/2);

nArray = array; % output array

F = zeros(m + 1,1); % length (m+1)
S = zeros(length(array) - m + 1, 1); % length (n-m+1)
F(1:m) = array(1:m);
S(1:n-m) = array(m+1:n);
F(m+1) = Inf;
S(n-m+1) = Inf;

i = 1;
j = 1;
for k = 1: n
    if F(i) <= S(j)
        nArray(k) = F(i);
        i = i + 1;
    else
        nArray(k) = S(j);
        j = j + 1;
        c = c + (m - i) + 1;
    end
end