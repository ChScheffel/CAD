function [ P, best_individual ] = ga_fx( dataStruct )
%GA_FX Summary of this function goes here
%   Detailed explanation goes here

best_individual = 1;

%% preallocation

P.A = struct('G', zeros(1,length(dataStruct.data)), 'F', 0);
% P=population of the iteration, A=individual, G=genotyp (parameter set), F=Fit , S=sigma

%% create the initial population

% create index vector
G = 1:dataStruct.clusters;
G = repmat(G, [1,length(dataStruct.data)/dataStruct.clusters]);

for i=1:dataStruct.n_init
    
    P(1).A(i).G = G(randperm(numel(G))); % shuffled index vector
    
    P(1).A(i).F = dataStruct.ObjFun(P(1).A(i).G, dataStruct.data); % calculate the fit
    
end

%loop through the maximum number of iterations
for iter=1:dataStruct.iterations
    
    %% generate new individuals through gauss-mutation
    
    B = struct('G', zeros(1,length(dataStruct.data)), 'F', 0); % the new individuals
    
    selection_prob = [P(iter).A.F]; % get the fits of the former population
    
    % the selection process is markov-chain inspired
    % check if all individuals don't have the same fit
    if length(unique(selection_prob))~=1
        selection_prob = sum(selection_prob)./selection_prob; % scale the fits (-> the best fit get's the highest value)
        selection_prob = selection_prob-min(selection_prob); % normalization to 0-1
        selection_prob = selection_prob/max(selection_prob);
        selection_prob = selection_prob*(1-.1)+.1; % normalization to 1-.1(also the least best fitting individuals have a chance to be selected)
    end
    selection_prob = selection_prob/sum(selection_prob); % scale so that the sum will be 1
    selection_prob = cumsum(selection_prob);
    
    for i=1:dataStruct.n_new
        % select random parent individual
        r = rand();
        B(i) = P(iter).A(find(selection_prob>r,1));
        
        % mutation
        for m=1:dataStruct.sig
            shuffle_idx = randperm(length(G), 2);
            B(i).G(shuffle_idx([2, 1])) = B(i).G(shuffle_idx);
        end
        
        % calculate fit
        B(i).F = dataStruct.ObjFun(B(i).G, dataStruct.data);
        
        if isnan(B(i).F)
            B(i) = [];
        end
        
    end %i
    
    %% step 4: select the best new individuals as new population via comma-selection
    
    [~, idx] = sort([B.F]); %, 'descend');
    
    for i=randperm(dataStruct.n_init)
        P(iter+1).A(i) = B(idx(i));
    end %i
    
    disp({'Iteration: ', iter, ' ObjFun=', P(iter+1).A(1).F});
    
    % save the population number if the best individual is the best until
    % now
    
    if P(iter+1).A(1).F < P(best_individual).A(1).F
        best_individual = iter+1;
    end

end %iter

disp({'best individual at population ', best_individual})


end

