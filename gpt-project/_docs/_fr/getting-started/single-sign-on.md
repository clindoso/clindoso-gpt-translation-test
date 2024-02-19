---
title: Authentification unique (SSO)
product_label:
  - advanced
  - enterprise
description: Apprenez à configurer et utiliser la SSO dans injixo.
---

La SSO est un mécanisme d’authentification permettant aux utilisateurs de se connecter à plusieurs applications et sites Internet à l’aide d’identifiants uniques. Une relation d’approbation est établie entre un service de gestion d’identité (fournisseur d’identité/IdP) central et une application (fournisseur de service/SP), ici injixo.

L’IdP est un produit tiers, tel que OneLogin, Microsoft Azure AD, Okta ou Google. L’utilisation de la SSO signifie que votre organisation bénéficiera de politiques de sécurité alignées, telles que l’authentification à deux facteurs et la rotation des mots de passe. Les utilisateurs s’authentifient auprès de l’IdP qui redirige vers injixo.

La configuration de l’IdP a été testée avec les IdP mentionnés ci-dessus. Si vous ne pouvez pas intégrer votre IdP spécifique, veuillez nous contacter.

## Prérequis techniques

Pour intégrer injixo au fournisseur d’identité de votre choix, les conditions suivantes doivent être remplies&nbsp;:

- prise en charge du protocole SAML 2.0,
- accès aux URL de métadonnées de fédération via Internet,
- l’adresse e-mail enregistrée dans injixo et votre IdP doivent être connectés à une boîte mail.

> Pour renforcer la sécurité, activez les assertions chiffrées/le cryptage des jetons (fortement recommandé).

## Activer la SSO pour votre compte

Seuls les utilisateurs disposant d’un accès admin peuvent activer la SSO.

1. Enregistrez injixo en tant que nouvelle application SAML ou SSO dans votre IdP.  
   Vous pouvez télécharger [ce logo injixo](/assets/img/common/injixo-logo.png) pour l’ajouter à la page de l’application web.

2. Dans injixo, accédez à _Account > Sécurité_{:.breadcrumbs} et configurez la SSO dans la section **Authentification unique**.

3. Dans la section **Métadonnées SAML injixo**, vous avez deux possibilités, en fonction de la prise en charge du téléchargement de fichiers de votre IdP&nbsp;:

   - Si le téléchargement de fichiers est pris en charge&nbsp;: cliquez sur _{% icon download | icon-only %} Télécharger_{:.doc-button} et complétez la configuration de l’IdP avec le fichier XML téléchargé.
   - Si le téléchargement de fichiers n’est pas pris en charge&nbsp;: cliquez sur **Détails du fournisseur de services** et ajoutez les URL à la configuration de votre IdP.

4. (Facultatif) Si vous utilisez des assertions SAML chiffrées, cliquez sur _{% icon download | icon-only %}Télécharger_{:.doc-button} dans la section **Chiffrement des jetons**. Ajoutez les certificats téléchargés à la configuration de votre IdP.
5. Selon la capacité de votre IdP à fournir une URL pour les métadonnées de fédération, terminez la configuration en suivant ces étapes&nbsp;:

   - Si votre IdP fournit une URL de métadonnées de fédération&nbsp;: copiez votre URL de métadonnées de fédération pour l’application enregistrée depuis votre IdP. Collez l’URL dans le champ **Federation Metadata URL** dans la section **Fournisseur d'identité (IdP)**.
   - Si votre IdP ne fournit pas d’URL de métadonnées de fédération&nbsp;: téléchargez le fichier XML de métadonnées de fédération et hébergez-le vous-même. À titre d’exemple, apprenez à configurer votre propre [application SAML personnalisée avec Google](https://support.google.com/a/answer/6087519?hl=en).

6. Cliquez sur _Enregistrer la configuration_{:.doc-button}.  
   > La SSO est maintenant active  
   >  
   > Les utilisateurs peuvent toujours se connecter avec leur nom d’utilisateur et leur mot de passe. Pour désactiver à nouveau la SSO, cliquez sur _Désactiver_{:.doc-button}.  
   > Pour augmenter le niveau de sécurité, [rendez obligatoire la SSO pour tous les utilisateurs](#rendre-obligatoire-la-sso-pour-tous-les-utilisateurs) après avoir testé la configuration dans l’étape suivante. 
   
## Tester la configuration de la SSO

Cliquez sur _Vérifier la configuration_{:.doc-button} pour tester la connexion via l’IdP. L’IdP génère une réponse SAML qui est envoyée à injixo. Vous serez redirigé vers la page de connexion de votre IdP, où vous devrez saisir les informations d’identification de l’IdP. Si la configuration de l’IdP est correcte et que le processus d’authentification réussit, vous serez connecté à injixo.

{{ 4 | image:  'Test de la configuration de la SSO réussi pour l’utilisateur actuel', '120%'  }}

### Le test a échoué&nbsp;?
<!-- A valid SubjectConfirmation was not found on this Response in our internal server logs -->

La réponse SAML de l’IdP contient l’assertion de l’utilisateur authentifié avec des attributs et des informations de profil. Si le processus échoue et que vous voyez un message d’erreur, vérifiez la configuration de l’application, la configuration de l’utilisateur et les attributs Recipient, InResponseTo, NotBefore et NotOnOrAfter définis dans l’IdP. 

Vous pouvez déboguer l’élément XML SubjectConfirmation dans la réponse SAML à l’aide des outils de développement de votre navigateur ou d’outils SAML externes. Pour voir la réponse non chiffrée en texte brut, désactivez les assertions chiffrées.

Exemple de l’élément XML SubjectConfirmation dans une réponse SAML&nbsp;:

```
</saml:Subject>
    <saml:NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress">email@company.org</saml:NameID>
    <saml:SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer">
        <saml:SubjectConfirmationData NotOnOrAfter="2022-08-11T08:25:25Z"
            Recipient="https://www.injixo.com/sso/saml/acs"
            InResponseTo="_abcdefgh-0444-4567-abcd-abcdabcdabcd"
    />
    </saml:SubjectConfirmation>
</saml:Subject>
```

## Rendre obligatoire la SSO pour tous les utilisateurs

Pour vérifier si la configuration a réussi, vous pouvez désactiver toutes les connexions avec nom d’utilisateur et mot de passe en rendant la SSO obligatoire pour tous les utilisateurs. Cependant, vous devez vous assurer que&nbsp;:

- tous les utilisateurs d’injixo existent dans l’IdP et dans injixo,
- l’e-mail injixo correspond bien à l’identifiant de l’IdP,
- tous les utilisateurs d’injixo sont assignés à l’application SSO d’injixo dans l’IdP.

Une fois la SSO rendue obligatoire, il n’est plus possible de&nbsp;:

- se connecter à l’aide d’un nom d’utilisateur et d’un mot de passe (tous les mots de passe existants seront invalidés),
- réinitialiser les mots de passe dans injixo (ni par l’utilisateur ni par l’administrateur),
- gérer l’accès à injixo hors IdP.

Vous pouvez rendre obligatoire la SSO dans la section **3. Activation**. Vous pourrez sélectionner le bouton _Activer_{:.doc-button} après avoir testé votre configuration SSO avec succès.

{{ 5 | image:  'Bouton pour rendre obligatoire la SSO pour tous les utilisateurs', '80%'  }}

## Modifier les adresses e-mail lorsque la SSO est activée

Lorsque la SSO est activée, les utilisateurs ne peuvent pas modifier leur adresse e-mail eux-mêmes car l’adresse e-mail injixo doit correspondre à l’identifiant de l’IdP approprié.

Seuls les utilisateurs avec un compte Admin peuvent modifier les adresses e-mail dans injixo.

## Se connecter à l’aide de la SSO

Lorsque la SSO est configurée, vos utilisateurs peuvent se connecter via [https://www.injixo.com/login/sso](https://www.injixo.com/login/sso). Ils devront saisir leur adresse e-mail et seront redirigés vers l’écran de connexion de l’IdP. Si les utilisateurs sont déjà connectés, ils seront automatiquement redirigés vers injixo. Sinon, ils devront saisir le mot de passe de l’IdP.

## Révoquer l’accès à injixo

Pour révoquer l’accès d’un utilisateur à injixo via la SSO, vous devez supprimer l’affectation de l’utilisateur injixo dans l’IdP. Remarque&nbsp;: si l’utilisateur existe toujours dans injixo, il sera toujours facturé. Pour éviter des coûts supplémentaires, vous devez également {% link_new désactiver ou supprimer l’utilisateur | features/administration/deactivate-employees.md %}.

## Désactiver la SSO

Pour désactiver le SSO et permettre à nouveau les connexions avec nom d’utilisateur et mot de passe, les utilisateurs ayant un accès admin peuvent désactiver la SSO. Cela supprimera la connexion IdP et tous les détails de configuration saisis. Une fois la SSO désactivée, tous les utilisateurs actifs recevront un e-mail pour définir un nouveau mot de passe injixo. La connexion avec le nom d’utilisateur et le mot de passe via [https://www.injixo.com/login](https://www.injixo.com/login) est ensuite de nouveau possible.

## Utiliser la SSO sur plusieurs tenants

Si votre organisation possède plusieurs tenants injixo, et si vous souhaitez donner accès à certains ou à tous les utilisateurs à plus d’un tenant, la configuration SSO standard ne fonctionnera pas. Contactez votre consultant pour configurer la SSO pour ce cas particulier.

<!-- SSO for multiple tenants can be activated by the feature flag multi_tenant_sso, see also https://github.com/ivx/internal-support-documentation/tree/main/Cortex-->