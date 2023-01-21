RSsig=meanBOLDAll;
signal = RSsig(:,:,1)';  %% data for 1 trial (NON FILTERED DATA!)

N = 90;
Tmax = 2300;
flp = .03;           % lowpass frequency of filter
fhi = .07;           % highpass
npts = Tmax;            % total nb of points
delt = .392;            % sampling interval
k = 2;                  % 2nd order butterworth filter


for seed=1:N
    
    x = signal(seed,:);
    fnq = 1/(2*delt);       % Nyquist frequency
    Wn = [flp/fnq fhi/fnq]; % butterworth bandpass non-dimensional frequency
    [b,a] = butter(k,Wn);   % construct the filter
    timeserie(seed,:) = filtfilt(b,a,x);    % zero phase filter the data
    
end


for seed=1:N
    
    Xanalytic = hilbert(demean(timeserie(seed,:)));
    Phases(seed,:) = angle(Xanalytic);
    
end

T=11:Tmax-10;

for t=1:length(T)
    
    ku=sum(complex(cos(Phases(:,T(t))),sin(Phases(:,T(t)))))/N;
    syncAux(t)=abs(ku);
    phsyncAux(t)=angle(ku);
    stdsyncAux(t)=std(Phases(:,T(t)));
    
end


metastab=std(syncAux);


save '../data/dbg.mat'

%%% Dimension of your data, in this case, 10 minutes (sampling 2 min.) and 66 regions

N=90;
% Nrand=10;
Nrand=1;
Tmax=2300;
Nsub=size(RSsig,3);

%%%%%%%%%%%%%

kk3=1;
kk4=1;
kk5=1;
nk=1;


% syncConn=zeros(N,N,Tmax-20,Nsub);
syncConnBinary=zeros(N,N,Nsub);


sync=zeros(Tmax-20,Nsub);
phsync=zeros(Tmax-20,Nsub);
stdsync=zeros(Tmax-20,Nsub);

timeserie=zeros(N,Tmax);
Phases=zeros(N,Tmax);
% syncConnAux=zeros(N,N,Tmax-20);
syncConnBinaryAux=zeros(N,N);





for s=1:Nsub
    
    tic;
    
    disp(['Hilbert Processing subject ',num2str(s)]);
    
    timeserie=zeros(N,Tmax);
    Phases=zeros(N,Tmax);
    %     syncConnAux=zeros(N,N,Tmax-20);
    syncConnBinaryAux=zeros(N,N);
    
    
    signal=RSsig(:,:,s)';  %% data for 1 trial (NON FILTERED DATA!)
    flp = .03;           % lowpass frequency of filter
    fhi = .07;           % highpass
    npts = Tmax;            % total nb of points
    delt = .392;            % sampling interval
    k=2;                  % 2nd order butterworth filter
    
    for seed=1:N
        
        x=signal(seed,:);
        fnq=1/(2*delt);       % Nyquist frequency
        Wn=[flp/fnq fhi/fnq]; % butterworth bandpass non-dimensional frequency
        [b,a]=butter(k,Wn);   % construct the filter
        timeserie(seed,:) = filtfilt(b,a,x);    % zero phase filter the data
        
    end
    
    %%%% Signal is already filtered:
    
    %     timeserie=sigFilt(:,:,s)';
    
    %%%% Calculate the phases
    
    
    
    for seed=1:N
        
        Xanalytic = hilbert(demean(timeserie(seed,:)));
        Phases(seed,:) = angle(Xanalytic);
        
    end
    
    %     T=10:Tmax-10;
    
    T=11:Tmax-10;
    
    %%%% Calculate Kuramoto order parameter (also interesting to plot...)
    
    syncAux=zeros(length(T),1);
    phsyncAux=zeros(length(T),1);
    stdsyncAux=zeros(length(T),1);
    
    
    
    for t=1:length(T)
        
        ku=sum(complex(cos(Phases(:,T(t))),sin(Phases(:,T(t)))))/N;
        syncAux(t)=abs(ku);
        phsyncAux(t)=angle(ku);
        stdsyncAux(t)=std(Phases(:,T(t)));
        
    end
    
    sync(:,s)=syncAux;
    
    phsyncAux(:,s)=phsyncAux;
    
    stdsync(:,s)=stdsyncAux;
    
    metastab(s)=std(syncAux);
    
    
    
    toc;
    
end



function [x] = hilbert(xr)

% Computes analytic signal

% FORMAT [x] = hilbert(xr)

%

% Returns analytic signal x = xr + i*xi such that

% xi is the Hilbert transform of real vector xr.

%__________________________________________________________________________

% Copyright (C) 2009 Wellcome Trust Centre for Neuroimaging



% Will Penny

% $Id$



if ~isreal(xr)

  xr = real(xr);

end



% Work along the first nonsingleton dimension

[xr,nshifts] = shiftdim(xr);



n = size(xr,1);

x = fft(xr,n,1); % n-point FFT over columns.

h  = zeros(n,~isempty(x)); % nx1 for nonempty. 0x0 for empty.

if n > 0 && 2*fix(n/2) == n

  % even and nonempty

  h([1 n/2+1]) = 1;

  h(2:n/2) = 2;

elseif n>0

  % odd and nonempty

  h(1) = 1;

  h(2:(n+1)/2) = 2;

end

x = ifft(x.*h(:,ones(1,size(x,2))));



% Convert back to the original shape.

x = shiftdim(x,-nshifts);

end

function c=adif(a,b)

if abs(a-b)>pi

  c=2*pi-abs(a-b);

else

  c=abs(a-b);

end

end
