from dataclasses import dataclass, field
from datetime import timedelta
from random import SystemRandom
from typing import Any, Callable, NewType, Union

from django.conf import settings as django_settings
import strawberry


def default_text_factory():
    return "".join(
        [
            str(node)
            for node in [
                SystemRandom().randint(0, 10) for _ in range(5, SystemRandom().randint(10, 20))
            ]
        ]
    )


_USER_NODE_FILTER_fieldS = {
    "email": ["exact"],
    "username": ["exact", "icontains", "istartswith"],
    "is_active": ["exact"],
    "status__archived": ["exact"],
    "status__verified": ["exact"],
    "status__secondary_email": ["exact"],
}

DjangoSetting = NewType("DjangoSetting", Union[dict, list, str, Any])


@dataclass
class GqlAuthSettings:
    # if allow logging in without verification,
    # the register mutation will return a token
    ALLOW_LOGIN_NOT_VERIFIED: bool = False
    # mutation fields options
    LOGIN_OPTIONAL_FIELDS: list = field(default_factory=lambda: [])
    LOGIN_REQUIRE_CAPTCHA: bool = True
    LOGIN_REQUIRED_FIELDS: Union[dict, list] = field(
        default_factory=lambda: ["username", "password"]
    )
    # required fields on register, plus password1 and password2,
    # can be a dict like UPDATE_MUTATION_fieldS setting
    REGISTER_MUTATION_FIELDS: Union[dict, list] = field(
        default_factory=lambda: ["email", "username"]
    )
    REGISTER_MUTATION_FIELDS_OPTIONAL: list = field(default_factory=lambda: [])
    REGISTER_REQUIRE_CAPTCHA: bool = True
    # captcha stuff
    CAPTCHA_EXPIRATION_DELTA: timedelta = timedelta(seconds=120)
    CAPTCHA_MAX_RETRIES: int = 5
    # any function that returns a string
    CAPTCHA_TEXT_FACTORY: Callable = default_text_factory
    # a function that receives the original string vs user input
    CAPTCHA_TEXT_VALIDATOR: Callable[[str, str], bool] = (
        lambda original, received: original == received
    )
    # will show captcha every time you create one
    FORCE_SHOW_CAPTCHA: bool = False
    # optional fields on update account, can be list of fields
    UPDATE_MUTATION_FIELDS: Union[dict, list] = field(
        default_factory=lambda: {"first_name": str, "last_name": str}
    )
    # tokens
    EXPIRATION_ACTIVATION_TOKEN: timedelta = timedelta(days=7)
    EXPIRATION_PASSWORD_RESET_TOKEN: timedelta = timedelta(hours=1)
    EXPIRATION_SECONDARY_EMAIL_ACTIVATION_TOKEN: timedelta = timedelta(hours=1)
    EXPIRATION_PASSWORD_SET_TOKEN: timedelta = timedelta(hours=1)
    # email stuff
    EMAIL_FROM: DjangoSetting = lambda: getattr(
        django_settings, "DEFAULT_FROM_EMAIL", "test@email.com"
    )
    SEND_ACTIVATION_EMAIL: bool = True
    # client: example.com/activate/token
    ACTIVATION_PATH_ON_EMAIL: str = "activate"
    ACTIVATION_SECONDARY_EMAIL_PATH_ON_EMAIL: str = "activate"
    # client: example.com/password-set/token
    PASSWORD_SET_PATH_ON_EMAIL: str = "password-set"
    # client: example.com/password-reset/token
    PASSWORD_RESET_PATH_ON_EMAIL: str = "password-reset"
    # email subjects templates
    EMAIL_SUBJECT_ACTIVATION: str = "email/activation_subject.txt"
    EMAIL_SUBJECT_ACTIVATION_RESEND: str = "email/activation_subject.txt"
    EMAIL_SUBJECT_SECONDARY_EMAIL_ACTIVATION: str = "email/activation_subject.txt"
    EMAIL_SUBJECT_PASSWORD_SET: str = "email/password_set_subject.txt"
    EMAIL_SUBJECT_PASSWORD_RESET: str = "email/password_reset_subject.txt"
    # email templates
    EMAIL_TEMPLATE_ACTIVATION: str = "email/activation_email.html"
    EMAIL_TEMPLATE_ACTIVATION_RESEND: str = "email/activation_email.html"
    EMAIL_TEMPLATE_SECONDARY_EMAIL_ACTIVATION: str = "email/activation_email.html"
    EMAIL_TEMPLATE_PASSWORD_SET: str = "email/password_set_email.html"
    EMAIL_TEMPLATE_PASSWORD_RESET: str = "email/password_reset_email.html"
    EMAIL_TEMPLATE_VARIABLES: dict = field(default_factory=lambda: {})
    # query stuff
    USER_NODE_EXCLUDE_FIELDS: Union[dict, list] = field(
        default_factory=lambda: ["password", "is_superuser"]
    )
    USER_NODE_FILTER_FIELDS: dict = field(default_factory=lambda: _USER_NODE_FILTER_fieldS)
    # others
    # turn is_active to False instead
    ALLOW_DELETE_ACCOUNT: bool = False
    # mutation error type
    CUSTOM_ERROR_TYPE: strawberry.scalar = "gqlauth.bases.scalars.ExpectedErrorType"
    # registration with no password
    ALLOW_PASSWORDLESS_REGISTRATION: bool = False
    SEND_PASSWORD_SET_EMAIL: bool = False
