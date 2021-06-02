program name
    !This program 
        !Created by: Enrique Hurtado
        !Date: 21 December 2020
        !Latest update: 21 December 2020
        !History:
            !Date: 12/21/20 || Mod: Program written || By: Enrique Hurtado
        !Purpose: Gaussian fit
            !Specification: 
        !Notes:
    !!Code Begins!!

    use setup
    !use mylib
    implicit none
    integer :: i, iter , itmin
    real (dp) :: xstart (1: npar ), fstart , stepi , epsx , epsf, ii, jj
    real (dp), external :: least2

    open(unit = 2, file ='test.dat')
    open(unit = 3, file ='test.d')
    do i = 1, nsp
        read(2 ,*) ii, jj
        write (3, *) ii, jj
        xx(i)= ii
        yy(i)= jj
    end do
    close (unit = 2)
    close (unit = 3)

    minsp = 75
    maxsp = 311
    xstart (1: npar ) = (/ 1.0, 7., 5000. , 0.2 , 0.3  /)
    !minsp = 1
    !maxsp = 16
    !xstart (1: npar ) = (/ 0., 0.09, 1. , 0.00038 , 0.00004  /)
    ifcal = 0
    iprint = 1
    fstart = least2 ( xstart (1: npar ))
    !stop
    itmin = 200
    iter = 2000
    epsf = 0.001_dp
    stepi = 0.1_dp
    iprint = 0

    minsp = 120
    maxsp = 200
    !print *, xstart
    call downhill (npar , least2 , xstart , fstart , &
                    stepi , epsf , itmin , iter )
    !print *, xstart
    iprint = 2
    fstart = least2 ( xstart (1: npar ))
    !print *, ifcal
    print *, xstart, fstart

end program name


function least2(par) result(ss)

    use setup
    implicit none
    real (dp) :: par(npar), a, b, y1, x1, sig1, ss, fi, step, x
    integer :: i, n

    ifcal = ifcal +1
    a = par (1); b = par (2)
    y1 = par(3); x1 = par(4); sig1 = par(5)

    ss = 0._dp
    do i = minsp , maxsp
        fi = a*xx(i) + b + y1*exp( -((xx(i)-x1 )/ sig1 )**2)
        ss = ss + 1./sqrt(yy(i)+2._dp) * (yy(i)-fi )**2
        !print*, i, fi, ss, xx(i), yy(i)
    end do
    ss = ss/abs(maxsp - minsp )
    !print *, ss
    !print *,ifcal ,par (1: npar ),ss
    !print '(i5 ,5 f12.4, f20 .5) ', ifcal ,par (1: npar ),ss
    write (8 ,*) ifcal, ss, ss

    n = 10000
    step = (xx(maxsp)-xx(minsp))/n
    x = xx(minsp)
    if ( iprint /= 0 ) then
        do i = 1 , n
            fi = a*x + b + y1*exp( -((x-x1 )/ sig1 )**2)
            write (unit =iprint ,fmt=*) x, fi
            x = x + step
        end do
    end if

end function least2

