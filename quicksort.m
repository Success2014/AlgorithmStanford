% [data] = textread('input3.txt');

function [nArray num] = quicksort(array)
% nArray is the new array
% c is the number of comparisons

n = length(array);

if n <= 1
    nArray = array;
    num = 0;
else
    c = n - 1;
%     [nArray0 pp] = partition1(array);
%     [nArray0 pp] = partition2(array);
    [nArray0 pp] = partition3(array);
    
    [nArray1 c1] = quicksort(nArray0(1:pp-1));
    [nArray2 c2] = quicksort(nArray0(pp+1:end));
    
    num = c + c1 + c2;
    nArray = [nArray1 nArray0(pp) nArray2];
    
end


