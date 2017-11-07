function Y = my_dft(X,n,dim)

if ~exist('dim','var')
	[ ~,dim] = max( [size(X,1), size(X,2)]);
end

if ~exist('n','var') || isequal(n,[])
	n = size(X,dim);
elseif dim==1
	X = X(1:n,:);
elseif dim==2
	X = X(:,1:n);
end

omega = exp(-2*pi*1i/n);
W = zeros(n,n);
for i = 2:n
	W(i,:) = [0:i-1:(i-1)*(n-1)];
end
W = bsxfun(@power, omega, W);


if dim == 2
	Y = X*W;
elseif dim==1
	Y = W*X;
end
end
