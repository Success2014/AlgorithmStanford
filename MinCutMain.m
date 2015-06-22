% Karger Min cut main
clear,clc
data_o = importdata('kargerMinCut-n.txt','\t'); % read data
% data_o = importdata('test6-3.txt','\t');
data = data_o(2:end,:);

% max_num_col = 10;
% format = repmat('%f',1,max_num_col);
% fid = fopen('test10.txt','rt');
% TMP = textscan(fid,format,'EmptyValue',NaN);
% fclose(fid);
% data = [];
% for i = 1:max_num_col
%     data = [TMP{:}];
% end


[n c]= size(data);               % number of vertices in the graph
N = n^2;                        % number of experiments to carry out
test = zeros(N,1);


for k = 1:N
    k
    
    list = cell(n,1);               % creat empty list
    
    for i = 1:n
        for j = 1:c
            if ~isnan(data(i,j)) && data(i,j) ~= i
                list{i} = [list{i} data(i,j)];
            end
        end
    end
    
% % %     min_deg = Inf; % minimum degree of vertices
% % %     for i = 1:n
% % %         if length(list{i}) < min_deg
% % %             min_deg = length(list{i})
% % %         end
% % %     end
    
    initial_state = k;
    test(k) = karger(list, initial_state);
end

min_cut = min(test)