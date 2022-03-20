APPNAME   = cotatenis-crawl-artwalk
VERSION   = 0.6.0

docker-build-staging:
	@sudo docker build \
        -t gcr.io/cotatenis/${APPNAME}:latest .

docker-build-production:
	@sudo docker build \
        -t gcr.io/cotatenis/${APPNAME}:${VERSION} .

docker-publish-staging:
	@sudo docker push gcr.io/cotatenis/${APPNAME}:latest

docker-publish-production:
	docker push gcr.io/cotatenis/${APPNAME}:${VERSION}

tag:
	@git tag v$(VERSION) && git push origin v$(VERSION)

delete-tag:
	@git push --delete origin v$(VERSION) && git tag --delete v$(VERSION)
