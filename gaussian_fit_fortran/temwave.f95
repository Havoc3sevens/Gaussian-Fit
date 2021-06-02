module twave
    use setup
    implicit none
    !This contains functions used in the main routine
        !Created by: Enrique Hurtado
        !Date: 15 April 2019
        !Latest update: 15 April 2019
        !History:
            !Date: 04/15/19 || Mod: Program written || By: Enrique Hurtado
        !Purpose:
            !Specification: 
        !Notes:
    !!Code Begins!!
    contains
        function hermite(x,n)
            integer :: n, i
            real(dp) :: x, hermite, hp(0:n)

            hp = 0._dp

            hp(0) = 1._dp
            hp(1) = 2._dp*x

            do i = 0, n-2
                hp(i+2) = 2._dp*x*hp(i+1) - 2._dp*(i+1)*hp(i)
            end do

            hermite = hp(n)

        end function

        function omega(z)
            real(dp) :: omega, z

            omega = w0*w0*(1.0 + (z*z)/(z0*z0))
        end function

        function R(z)
            real(dp) :: R, z

            R = z*(1.0 + (z0*z0)/(z*z))
        end function

        function Eta(z)
            real(dp) :: Eta, z

            Eta = atan(z/z0)
        end function

        function Ep(x,y,z)
            real(dp) :: Ep, x, y, z

            Ep = E0*(w0/omega(z))*hermite(sqrt(2._dp)*x/omega(z),l)*&
            hermite(sqrt(2._dp)*y/omega(z),m)*exp(-(x*x+y*y)/omega(z)*omega(z))
            
        end function

end module
