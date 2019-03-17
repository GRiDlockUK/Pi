
ver() {
 lsb_id=$(lsb_release -si)
 lsb_desc=$(lsb_release -sd) 
 lsb_codename=$(lsb_release -sc) 
 echo $lsb_desc
}

ver;


