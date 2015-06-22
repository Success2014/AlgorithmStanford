% karger min cut algorithm

function min_cut = karger(list, initial_state)

% n = length(list); % number of vertices
% e = 0; % number of edges
% for i = 1 : n
%     e = e + length(list{i});
% end
% e = e / 2;
min_cut = 0;

while sum(~cellfun('isempty',list)) > 2 % nonempty
%     min_cut = min_cut - 1;
%     sta = RandStream.create('mt19937ar','seed',27 + initial_state); 
%     RandStream.setDefaultStream(sta);
    
    choose_able = find(~cellfun('isempty',list));
    t = choose_able(randi(length(choose_able),1)); % randomly select one endpoint of the edge to contract
    tmp_index = randi(length(list{t}),1); % index of other endpoint of the edge to contract
    s = list{t}(tmp_index); % the other endpoint of the edge to contract
    
    % contract edges, delete all endpoints with s
    list{t}(find(list{t}==s)) = [];
    
    %--Add points
    for j = 1:length(list{s})
%         if list{s}(j) ~= t && ~ismember(list{s}(j), list{t}) % if not the contracted and existing point
        if list{s}(j) ~= t 
            list{t} = [list{t} list{s}(j)];  % Points connected to the contracted point, then add them to the new list
        end
    end
    
    %--Change index
    for i = 1 : length(list)
        if i == s
            list{i} = [];
        else
            for j = 1:length(list{i})
                if list{i}(j) == s
                    list{i}(j) = t;
                end
            end
        end
    end
    
%     list = list(~cellfun('isempty',list));
    
    
end


for i = 1:length(list)
    if length(list{i}) > min_cut
        min_cut = length(list{i});
    end
end




