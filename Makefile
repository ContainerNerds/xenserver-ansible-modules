ANSIBLE_GROUP = ansible
init:
	mkdir -p ./build/usr/share/ansible/modules
	cp -r ./ansible-modules/module_utils ./build/usr/share/ansible/
	cp -r ./ansible-modules ./build/usr/share/ansible/modules/xenserver
install:
	cp -r ./build/usr /
uninstall:
	rm -rf /usr/share/ansible/modules/xenserver
clean:
	find . -iname *.pyc -exec rm -f {} +
	rm -rf ./build
