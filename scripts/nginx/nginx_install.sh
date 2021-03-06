#!/bin/bash
# Author Yo
# Email YoLoveLife@outlook.com
# Time 2017-02-07 11:27
PATH=/bin:/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin
VERSION="1.10.1"
PREFIX="/usr/local"
BASEDIR=${PREFIX}/nginx
YESFLAG="0"
USER="www"
function Confirm()
{
cat <<_ACEOF
	Version:	${VERSION}
	Prefix:		${PREFIX}
_ACEOF
}
function IsAlready()
{
	if [ -d "/usr/local/nginx" ];then
		echo "001001002"
		exit 2
	fi
}
function Help()
{
cat <<_ACEOF
configure nginx_install bash script.
Usage $0 [OPTION]... [VAR=VALUE]...
        --help          display this help and exit
        -v,--version    modify the version of nginx.Default 1.10.1
        -f,--prefix     modify the prefix.Default /usr/local
_ACEOF
}
function Avrg()
{
	ARGS=`getopt -o v:f: --long version:,prefix: -n 'nginx_install.sh' -- "$@"`
	if [ ! $? -eq 0 ];then
		echo "001002002"
		exit 2
	fi
	eval set -- "${ARGS}"

	while true
	do
		case "$1" in
			-v|--version)
				VERSION=$2
				shift 2
				;;
			-f|--prefix)
				PREFIX=$2
				shift 2
				;;
			--)
				shift
				break
				;;
			*)
				#Help
				echo "参数错误"
				exit 2
			esac
	done
}
IsAlready
if [ "$1" == '--help' ];then
	Help
	exit 2
fi
Avrg $@

if [ `cat /etc/passwd |grep ${USER}|wc -l` == "0" ];then
    groupadd ${USER}
    useradd -s ${SHELL} -g ${USER} ${USER}
fi

FILENAME=nginx-${VERSION}

tar -xvzf ${FILENAME}.tar.gz &>/dev/null
cd ./${FILENAME}

mkdir -p ${PREFIX}/nginx

./configure --prefix=${PREFIX}/nginx --user=${USER} --group=${USER}&>/dev/null
make &>/dev/null
make install &> /dev/null

chown ${USER}:${USER} ${PREFIX}/nginx

#Confirm > ${PREFIX}/nginx/INSTALL.info

echo "001000000"
