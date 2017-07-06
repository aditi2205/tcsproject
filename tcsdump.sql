--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.7
-- Dumped by pg_dump version 9.6.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE auth_group OWNER TO root;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_group_id_seq OWNER TO root;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE auth_group_permissions OWNER TO root;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_group_permissions_id_seq OWNER TO root;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE auth_permission OWNER TO root;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_permission_id_seq OWNER TO root;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE auth_user OWNER TO root;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE auth_user_groups OWNER TO root;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_groups_id_seq OWNER TO root;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_id_seq OWNER TO root;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE auth_user_user_permissions OWNER TO root;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_user_permissions_id_seq OWNER TO root;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE django_admin_log OWNER TO root;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_admin_log_id_seq OWNER TO root;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE django_content_type OWNER TO root;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_content_type_id_seq OWNER TO root;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE django_migrations OWNER TO root;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_migrations_id_seq OWNER TO root;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE django_migrations_id_seq OWNED BY django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE django_session OWNER TO root;

--
-- Name: portal_personaldetails; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE portal_personaldetails (
    "Pid" integer NOT NULL,
    "Name" character varying(20) NOT NULL,
    "Gender" character varying(20) NOT NULL,
    "RelationshipStatus" character varying(20) NOT NULL,
    "Occupation" character varying(20) NOT NULL,
    "Student" character varying(20) NOT NULL,
    "City" character varying(20) NOT NULL,
    "Age" integer NOT NULL,
    "Email_id" character varying(50)
);


ALTER TABLE portal_personaldetails OWNER TO root;

--
-- Name: portal_personaldetails_Pid_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE "portal_personaldetails_Pid_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "portal_personaldetails_Pid_seq" OWNER TO root;

--
-- Name: portal_personaldetails_Pid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE "portal_personaldetails_Pid_seq" OWNED BY portal_personaldetails."Pid";


--
-- Name: portal_responses; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE portal_responses (
    q1 integer NOT NULL,
    q2 integer NOT NULL,
    q3 integer,
    q4 integer,
    q5 integer,
    q10 integer,
    q11 integer,
    q12 integer,
    q13 integer,
    q14 integer,
    q15 integer,
    q16 integer,
    q17 integer,
    q18 integer,
    q19 integer,
    q20 integer,
    q21 integer,
    q6 integer,
    q7 integer,
    q8 integer,
    q9 integer,
    person_id integer NOT NULL,
    result integer NOT NULL
);


ALTER TABLE portal_responses OWNER TO root;

--
-- Name: portal_responses_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE portal_responses_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE portal_responses_id_seq OWNER TO root;

--
-- Name: portal_result; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE portal_result (
    "Rid_id" integer NOT NULL,
    result integer NOT NULL
);


ALTER TABLE portal_result OWNER TO root;

--
-- Name: portal_result_Rid_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE "portal_result_Rid_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "portal_result_Rid_seq" OWNER TO root;

--
-- Name: portal_story; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE portal_story (
    storyid integer NOT NULL,
    name character varying(50) NOT NULL,
    age integer NOT NULL,
    location character varying(30) NOT NULL,
    story_text text NOT NULL,
    "time" timestamp with time zone
);


ALTER TABLE portal_story OWNER TO root;

--
-- Name: portal_stories_Storyid_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE "portal_stories_Storyid_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "portal_stories_Storyid_seq" OWNER TO root;

--
-- Name: portal_stories_Storyid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE "portal_stories_Storyid_seq" OWNED BY portal_story.storyid;


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY django_migrations ALTER COLUMN id SET DEFAULT nextval('django_migrations_id_seq'::regclass);


--
-- Name: portal_personaldetails Pid; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY portal_personaldetails ALTER COLUMN "Pid" SET DEFAULT nextval('"portal_personaldetails_Pid_seq"'::regclass);


--
-- Name: portal_story storyid; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY portal_story ALTER COLUMN storyid SET DEFAULT nextval('"portal_stories_Storyid_seq"'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: root
--



--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('auth_group_id_seq', 1, false);


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: root
--



--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 1, false);


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: root
--

INSERT INTO auth_permission VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO auth_permission VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO auth_permission VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO auth_permission VALUES (4, 'Can add group', 2, 'add_group');
INSERT INTO auth_permission VALUES (5, 'Can change group', 2, 'change_group');
INSERT INTO auth_permission VALUES (6, 'Can delete group', 2, 'delete_group');
INSERT INTO auth_permission VALUES (7, 'Can add permission', 3, 'add_permission');
INSERT INTO auth_permission VALUES (8, 'Can change permission', 3, 'change_permission');
INSERT INTO auth_permission VALUES (9, 'Can delete permission', 3, 'delete_permission');
INSERT INTO auth_permission VALUES (10, 'Can add user', 4, 'add_user');
INSERT INTO auth_permission VALUES (11, 'Can change user', 4, 'change_user');
INSERT INTO auth_permission VALUES (12, 'Can delete user', 4, 'delete_user');
INSERT INTO auth_permission VALUES (13, 'Can add content type', 5, 'add_contenttype');
INSERT INTO auth_permission VALUES (14, 'Can change content type', 5, 'change_contenttype');
INSERT INTO auth_permission VALUES (15, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO auth_permission VALUES (16, 'Can add session', 6, 'add_session');
INSERT INTO auth_permission VALUES (17, 'Can change session', 6, 'change_session');
INSERT INTO auth_permission VALUES (18, 'Can delete session', 6, 'delete_session');
INSERT INTO auth_permission VALUES (19, 'Can add result', 7, 'add_result');
INSERT INTO auth_permission VALUES (20, 'Can change result', 7, 'change_result');
INSERT INTO auth_permission VALUES (21, 'Can delete result', 7, 'delete_result');
INSERT INTO auth_permission VALUES (22, 'Can add personaldetails', 8, 'add_personaldetails');
INSERT INTO auth_permission VALUES (23, 'Can change personaldetails', 8, 'change_personaldetails');
INSERT INTO auth_permission VALUES (24, 'Can delete personaldetails', 8, 'delete_personaldetails');
INSERT INTO auth_permission VALUES (25, 'Can add forum', 9, 'add_forum');
INSERT INTO auth_permission VALUES (26, 'Can change forum', 9, 'change_forum');
INSERT INTO auth_permission VALUES (27, 'Can delete forum', 9, 'delete_forum');
INSERT INTO auth_permission VALUES (28, 'Can add responses', 10, 'add_responses');
INSERT INTO auth_permission VALUES (29, 'Can change responses', 10, 'change_responses');
INSERT INTO auth_permission VALUES (30, 'Can delete responses', 10, 'delete_responses');
INSERT INTO auth_permission VALUES (31, 'Can add stories', 11, 'add_stories');
INSERT INTO auth_permission VALUES (32, 'Can change stories', 11, 'change_stories');
INSERT INTO auth_permission VALUES (33, 'Can delete stories', 11, 'delete_stories');
INSERT INTO auth_permission VALUES (34, 'Can add story', 11, 'add_story');
INSERT INTO auth_permission VALUES (35, 'Can change story', 11, 'change_story');
INSERT INTO auth_permission VALUES (36, 'Can delete story', 11, 'delete_story');


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('auth_permission_id_seq', 36, true);


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: root
--

INSERT INTO auth_user VALUES (1, 'pbkdf2_sha256$36000$GaW3KYQK9KeX$jELpmE+NxFjEUlp83OmfKtjkYsb9XIZLL8fy9/Gfbfc=', '2017-06-26 07:42:17.671639+00', true, 'ankita', '', '', 'ankita.sharma102@gmail.com', true, true, '2017-06-26 07:32:29.163687+00');


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: root
--



--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('auth_user_id_seq', 1, true);


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: root
--



--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: root
--

INSERT INTO django_admin_log VALUES (1, '2017-06-26 07:35:41.364041+00', '1', 'Stories object', 1, '[{"added": {}}]', 11, 1);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 1, true);


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: root
--

INSERT INTO django_content_type VALUES (1, 'admin', 'logentry');
INSERT INTO django_content_type VALUES (2, 'auth', 'group');
INSERT INTO django_content_type VALUES (3, 'auth', 'permission');
INSERT INTO django_content_type VALUES (4, 'auth', 'user');
INSERT INTO django_content_type VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO django_content_type VALUES (6, 'sessions', 'session');
INSERT INTO django_content_type VALUES (7, 'portal', 'result');
INSERT INTO django_content_type VALUES (8, 'portal', 'personaldetails');
INSERT INTO django_content_type VALUES (9, 'portal', 'forum');
INSERT INTO django_content_type VALUES (10, 'portal', 'responses');
INSERT INTO django_content_type VALUES (11, 'portal', 'story');


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('django_content_type_id_seq', 11, true);


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: root
--

INSERT INTO django_migrations VALUES (1, 'contenttypes', '0001_initial', '2017-06-23 08:37:44.322795+00');
INSERT INTO django_migrations VALUES (2, 'auth', '0001_initial', '2017-06-23 08:37:44.541717+00');
INSERT INTO django_migrations VALUES (3, 'admin', '0001_initial', '2017-06-23 08:37:44.619549+00');
INSERT INTO django_migrations VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2017-06-23 08:37:44.660437+00');
INSERT INTO django_migrations VALUES (5, 'contenttypes', '0002_remove_content_type_name', '2017-06-23 08:37:44.736182+00');
INSERT INTO django_migrations VALUES (6, 'auth', '0002_alter_permission_name_max_length', '2017-06-23 08:37:44.761192+00');
INSERT INTO django_migrations VALUES (7, 'auth', '0003_alter_user_email_max_length', '2017-06-23 08:37:44.797913+00');
INSERT INTO django_migrations VALUES (8, 'auth', '0004_alter_user_username_opts', '2017-06-23 08:37:44.837581+00');
INSERT INTO django_migrations VALUES (9, 'auth', '0005_alter_user_last_login_null', '2017-06-23 08:37:44.919197+00');
INSERT INTO django_migrations VALUES (10, 'auth', '0006_require_contenttypes_0002', '2017-06-23 08:37:44.924647+00');
INSERT INTO django_migrations VALUES (11, 'auth', '0007_alter_validators_add_error_messages', '2017-06-23 08:37:44.959993+00');
INSERT INTO django_migrations VALUES (12, 'auth', '0008_alter_user_username_max_length', '2017-06-23 08:37:45.002146+00');
INSERT INTO django_migrations VALUES (13, 'portal', '0001_initial', '2017-06-23 08:37:45.045553+00');
INSERT INTO django_migrations VALUES (14, 'portal', '0002_auto_20170610_0845', '2017-06-23 08:37:45.065963+00');
INSERT INTO django_migrations VALUES (15, 'portal', '0003_auto_20170610_0910', '2017-06-23 08:37:45.096392+00');
INSERT INTO django_migrations VALUES (16, 'portal', '0004_auto_20170611_1239', '2017-06-23 08:37:45.135037+00');
INSERT INTO django_migrations VALUES (17, 'portal', '0005_personaldetails_email_id', '2017-06-23 08:37:45.16571+00');
INSERT INTO django_migrations VALUES (18, 'portal', '0006_auto_20170619_1724', '2017-06-23 08:37:45.28062+00');
INSERT INTO django_migrations VALUES (19, 'portal', '0007_auto_20170619_1833', '2017-06-23 08:37:45.361625+00');
INSERT INTO django_migrations VALUES (20, 'portal', '0008_auto_20170620_0734', '2017-06-23 08:37:45.41438+00');
INSERT INTO django_migrations VALUES (21, 'portal', '0009_auto_20170620_0748', '2017-06-23 08:37:45.431384+00');
INSERT INTO django_migrations VALUES (22, 'portal', '0010_auto_20170620_1015', '2017-06-23 08:37:45.483962+00');
INSERT INTO django_migrations VALUES (23, 'portal', '0011_auto_20170620_1045', '2017-06-23 08:37:45.582396+00');
INSERT INTO django_migrations VALUES (24, 'portal', '0012_auto_20170620_1047', '2017-06-23 08:37:45.632751+00');
INSERT INTO django_migrations VALUES (25, 'portal', '0013_auto_20170620_1120', '2017-06-23 08:37:45.732275+00');
INSERT INTO django_migrations VALUES (26, 'portal', '0014_auto_20170620_1128', '2017-06-23 08:37:45.817917+00');
INSERT INTO django_migrations VALUES (27, 'portal', '0015_auto_20170620_1235', '2017-06-23 08:37:45.841626+00');
INSERT INTO django_migrations VALUES (28, 'portal', '0016_auto_20170621_0434', '2017-06-23 08:37:45.875492+00');
INSERT INTO django_migrations VALUES (29, 'portal', '0017_auto_20170621_0532', '2017-06-23 08:37:45.952609+00');
INSERT INTO django_migrations VALUES (30, 'sessions', '0001_initial', '2017-06-23 08:37:45.992846+00');
INSERT INTO django_migrations VALUES (31, 'portal', '0018_auto_20170623_0850', '2017-06-23 08:50:41.211033+00');
INSERT INTO django_migrations VALUES (32, 'portal', '0019_auto_20170623_0925', '2017-06-23 09:25:38.160117+00');
INSERT INTO django_migrations VALUES (33, 'portal', '0020_auto_20170626_1253', '2017-06-26 07:23:52.643478+00');
INSERT INTO django_migrations VALUES (34, 'portal', '0021_auto_20170626_1310', '2017-06-26 07:40:22.284921+00');
INSERT INTO django_migrations VALUES (35, 'portal', '0022_auto_20170626_1340', '2017-06-26 08:10:07.385908+00');
INSERT INTO django_migrations VALUES (36, 'portal', '0023_auto_20170630_0910', '2017-07-04 06:23:19.439196+00');
INSERT INTO django_migrations VALUES (37, 'portal', '0024_auto_20170704_1152', '2017-07-04 06:23:19.471971+00');
INSERT INTO django_migrations VALUES (38, 'portal', '0024_auto_20170704_1720', '2017-07-05 10:15:19.533794+00');
INSERT INTO django_migrations VALUES (39, 'portal', '0025_merge_20170705_1544', '2017-07-05 10:15:19.544896+00');
INSERT INTO django_migrations VALUES (40, 'portal', '0026_auto_20170705_1625', '2017-07-05 11:31:27.30505+00');
INSERT INTO django_migrations VALUES (41, 'portal', '0027_auto_20170705_1627', '2017-07-05 11:31:27.389764+00');
INSERT INTO django_migrations VALUES (42, 'portal', '0028_responses_result', '2017-07-05 11:31:27.423816+00');


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('django_migrations_id_seq', 42, true);


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: root
--

INSERT INTO django_session VALUES ('15osohl9ntkziiu44q295ati79govr07', 'M2UxZTM3YzViMzRlZDFkMmNhNjNlMDg4NzdlOTg3OWY4OGIzZmNmNTp7Il9hdXRoX3VzZXJfaGFzaCI6IjViZDM4MGUyNTc5NWMwOTllNTNjYjYzNGQzODY4MTU4ZjVjMGU5MGIiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwid2l6YXJkX2NvbnRhY3Rfd2l6YXJkIjp7InN0ZXBfZmlsZXMiOnt9LCJzdGVwIjoiMCIsImV4dHJhX2RhdGEiOnt9LCJzdGVwX2RhdGEiOnt9fX0=', '2017-07-10 08:14:16.656847+00');
INSERT INTO django_session VALUES ('is28ty9tjallzp6k03sahkgmqhnsibwk', 'NGI2YmIzZGYxNWQ3NTIyZjFhM2ZjMmE0MDg1ZDJlMWRhMDk4YTkzOTp7IndpemFyZF9jb250YWN0X3dpemFyZCI6eyJleHRyYV9kYXRhIjp7fSwic3RlcF9maWxlcyI6e30sInN0ZXBfZGF0YSI6e30sInN0ZXAiOm51bGx9LCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNWJkMzgwZTI1Nzk1YzA5OWU1M2NiNjM0ZDM4NjgxNThmNWMwZTkwYiJ9', '2017-07-20 07:47:14.614735+00');


--
-- Data for Name: portal_personaldetails; Type: TABLE DATA; Schema: public; Owner: root
--

INSERT INTO portal_personaldetails VALUES (12, 'Ankita Sharma', 'male', 'Single', 'NA', 'College', 'Delhi', 20, 'ankita.sharma102@gmail.com');
INSERT INTO portal_personaldetails VALUES (13, 'Ankita Sharma', 'male', 'Single', 'NA', 'College', 'Delhi', 20, 'ankita.sharma102@gmail.com');
INSERT INTO portal_personaldetails VALUES (14, 'Ankita Sharma', 'male', 'Single', 'NA', 'College', 'Delhi', 20, 'ankita.sharma102@gmail.com');
INSERT INTO portal_personaldetails VALUES (15, 'Ankita Sharma', 'male', 'Single', 'NA', 'College', 'Delhi', 20, 'ankita.sharma102@gmail.com');
INSERT INTO portal_personaldetails VALUES (16, 'Aditya Sharma', 'male', 'Single', 'NA', 'College', 'Delhi', 19, NULL);


--
-- Name: portal_personaldetails_Pid_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('"portal_personaldetails_Pid_seq"', 16, true);


--
-- Data for Name: portal_responses; Type: TABLE DATA; Schema: public; Owner: root
--

INSERT INTO portal_responses VALUES (2, 1, 2, 3, 1, 1, 1, 2, 1, 0, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 2, 13, 28);
INSERT INTO portal_responses VALUES (2, 1, 2, 3, 1, 1, 1, 2, 1, 0, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 2, 14, 28);
INSERT INTO portal_responses VALUES (2, 1, 2, 3, 1, 1, 1, 2, 1, 0, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 2, 15, 28);
INSERT INTO portal_responses VALUES (3, 0, 1, 1, 0, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 3, 16, 43);


--
-- Name: portal_responses_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('portal_responses_id_seq', 1, true);


--
-- Data for Name: portal_result; Type: TABLE DATA; Schema: public; Owner: root
--



--
-- Name: portal_result_Rid_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('"portal_result_Rid_seq"', 1, true);


--
-- Name: portal_stories_Storyid_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('"portal_stories_Storyid_seq"', 2, true);


--
-- Data for Name: portal_story; Type: TABLE DATA; Schema: public; Owner: root
--

INSERT INTO portal_story VALUES (1, 'Ankita Sharma', 20, 'Delhi, India', 'Hi, I am Ankita. Just testing this out.', '2017-06-26 07:35:08+00');
INSERT INTO portal_story VALUES (2, 'Ankita', 20, 'Mumbai, India', 'skcndlk', '2017-06-26 10:40:18.829459+00');


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: portal_personaldetails portal_personaldetails_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY portal_personaldetails
    ADD CONSTRAINT portal_personaldetails_pkey PRIMARY KEY ("Pid");


--
-- Name: portal_responses portal_responses_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY portal_responses
    ADD CONSTRAINT portal_responses_pkey PRIMARY KEY (person_id);


--
-- Name: portal_result portal_result_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY portal_result
    ADD CONSTRAINT portal_result_pkey PRIMARY KEY ("Rid_id");


--
-- Name: portal_story portal_stories_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY portal_story
    ADD CONSTRAINT portal_stories_pkey PRIMARY KEY (storyid);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX auth_group_name_a6ea08ec_like ON auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX auth_user_groups_group_id_97559544 ON auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX auth_user_username_6821ab7c_like ON auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX django_session_expire_date_a5c62663 ON django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: root
--

CREATE INDEX django_session_session_key_c0390e0f_like ON django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: portal_responses portal_responses_person_id_c3da6fb3_fk_portal_pe; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY portal_responses
    ADD CONSTRAINT portal_responses_person_id_c3da6fb3_fk_portal_pe FOREIGN KEY (person_id) REFERENCES portal_personaldetails("Pid") DEFERRABLE INITIALLY DEFERRED;


--
-- Name: portal_result portal_result_Rid_id_79a70199_fk_portal_personaldetails_Pid; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY portal_result
    ADD CONSTRAINT "portal_result_Rid_id_79a70199_fk_portal_personaldetails_Pid" FOREIGN KEY ("Rid_id") REFERENCES portal_personaldetails("Pid") DEFERRABLE INITIALLY DEFERRED;


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

