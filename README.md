# ExpCalculator

Exposure Time Calculator\
*Marek Gorski*\
*28.07.2022*  

**ToDo:**
* passband efficiency
* other bands (I,J,H,K)


**Reguirements:** *python3,  numpy, scipy*  

### Calculations:
Aperture = 2 * seeing 

**background:**

*pixel_size_coefficient*  = (*pix_size* / *reference_pix_size*)^2 \
*background_per_pix* = (*dark* + *sky_background* \* *pixel_size_coefficient* ) \* *exp_time* \
*number_of_pix_in_aperture* =  3.14 \* 2 \* (*seeing* / *pix_size*)^2 \
**background_in_aperture (2 \* seeing)** =  *background_per_pix* \* *number_of_pix_in_apertur*

**star ADU:** \
*reference_star_radiation* \
*magnitude_coefficient* = 10^(*reference_m* - *magnitude*)/2.5 \
*mirror_coefficient* = (*mirror_size*/*reference_mirror_size*)^2 \
**star_ADU** = *reference_star_radiation* \* *magnitude_coefficient* \* *mirror_coefficient* \* *exp_time* 

**noise:** \
**noise** = sqrt(*background_in_aperture* + *star_ADU*) + *readout_noise*

**Signal to Noise:** \
**sn** = *star_ADU* / *noise* 

**Pixel Saturation:** \
*sigma_coe* = *pix_size* / (*seeing*/2.355)  <-- fwhm=2.355 /* sigma \
*coe_norm* = CDF(*sigma_coe*)-CDF(-1\**sigma_coe*) \
**central_pixel_ADU** = *background_per_pix* + *star_ADU* /* *coe_norm*





