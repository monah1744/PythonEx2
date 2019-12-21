--
-- PostgreSQL database dump
--

-- Dumped from database version 12.1
-- Dumped by pg_dump version 12.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: m_city; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.m_city (
    id integer NOT NULL,
    title character varying(50)
);


ALTER TABLE public.m_city OWNER TO postgres;

--
-- Name: m_city_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.m_city_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.m_city_id_seq OWNER TO postgres;

--
-- Name: m_city_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.m_city_id_seq OWNED BY public.m_city.id;


--
-- Name: m_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.m_user (
    id integer NOT NULL,
    gender boolean,
    name character varying(50),
    email character varying(50),
    city_id integer
);


ALTER TABLE public.m_user OWNER TO postgres;

--
-- Name: m_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.m_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.m_user_id_seq OWNER TO postgres;

--
-- Name: m_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.m_user_id_seq OWNED BY public.m_user.id;


--
-- Name: m_city id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.m_city ALTER COLUMN id SET DEFAULT nextval('public.m_city_id_seq'::regclass);


--
-- Name: m_user id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.m_user ALTER COLUMN id SET DEFAULT nextval('public.m_user_id_seq'::regclass);


--
-- Data for Name: m_city; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.m_city (id, title) FROM stdin;
1	Kharkiv
2	Kyiv
3	Zhitomyr
4	Kharkiv
\.


--
-- Data for Name: m_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.m_user (id, gender, name, email, city_id) FROM stdin;
1	f	Aaron	Aaron@gmail.com	1
2	f	Nifont	Nifont@gmail.com	1
3	f	Favst	Favst@gmail.com	2
4	f	Liodor	Liodor@gmail.com	3
5	f	Terentiy	Terentiy@gmail.com	1
6	f	Denis	Denis@gmail.com	1
7	f	Ovdokim	Ovdokim@gmail.com	2
8	f	Elisey	Elisey@gmail.com	3
9	f	Gennadiy	Gennadiy@gmail.com	1
10	f	Harisiy	Harisiy@gmail.com	1
11	t	Kira	Kira@gmail.com	2
12	t	Olimpiada	Olimpiada@gmail.com	3
13	t	Vladlena	Vladlena@gmail.com	1
14	t	Inessa	Inessa@gmail.com	1
15	t	Praskovya	Praskovya@gmail.com	2
16	t	Lidiya	Lidiya@gmail.com	3
17	t	Zoya	Zoya@gmail.com	1
18	t	Iraida	Iraida@gmail.com	1
19	t	Kristina	Kristina@gmail.com	1
20	t	Beatrisa	Beatrisa@gmail.com	4
\.


--
-- Name: m_city_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.m_city_id_seq', 4, true);


--
-- Name: m_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.m_user_id_seq', 20, true);


--
-- PostgreSQL database dump complete
--

